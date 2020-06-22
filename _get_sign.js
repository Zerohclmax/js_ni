const express = require('express')
const app = express()							// 1    建一个Express应用程序
const get_sign = require("./baidu")					// 2	导入sum.js文件
var bodyParser = require('body-parser');		// 3	导入body-parser包
app.use(bodyParser());							// 4	定义中间件的意思撒

app.post('/get_sign',function (req,res) {
    let req_parma = req.body;
    console.log('req_parma:',req_parma)

    let word = req_parma.word

    sign = get_sign.get_sign(word)
    res.send(sign)
})

app.listen(3000, ()=>{
    console.log("开启服务")
})