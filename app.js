const pdfreader = require('pdfreader');
const fs = require("fs");

async function bufferize(url) {
    return new Promise((resolve,reject)=>{
        fs.readFile(url,(err,buffer)=>{
            resolve(buffer)
        })
    })
}

/*
if second param is set then a space ' ' inserted whenever text
chunks are separated by more than xwidth
this helps in situations where words appear separated but
this is because of x coords (there are no spaces between words)
 
each page is a different array element
*/
async function readlines(buffer, xwidth) {
    return new Promise((resolve, reject) => {
        var pdftxt = new Array();
        var pg = 0;
        new pdfreader.PdfReader().parseBuffer(buffer, function (err, item) {
            if (err) console.log("pdf reader error: " + err);
            else if (!item) {
                pdftxt.forEach(function (a, idx) {
                    pdftxt[idx].forEach(function (v, i) {
                        pdftxt[idx][i].splice(1, 2);
                    });
                });
                resolve(pdftxt);
            } else if (item && item.page) {
                pg = item.page - 1;
                pdftxt[pg] = [];
            } else if (item.text) {
                var t = 0;
                var sp = "";
                pdftxt[pg].forEach(function (val, idx) {
                    if (val[1] == item.y) {
                        if (xwidth && item.x - val[2] > xwidth) {
                            sp += " ";
                        } else {
                            sp = "";
                        }
                        pdftxt[pg][idx][0] += sp + item.text;
                        t = 1;
                    }
                });
                if (t == 0) {
                    pdftxt[pg].push([item.text, item.y, item.x]);
                }
            }
        });
    });
}

(async () => {
    var url ='./1.pdf';
    var buffer = await bufferize(url);
    var lines = await readlines(buffer);
    lines = await JSON.parse(JSON.stringify(lines));
    console.log(lines);
})();