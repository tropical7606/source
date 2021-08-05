import React, { useState, useEffect } from "react"
import styled from "styled-components";
import axios, { post } from 'axios';
function Braille_PDF_trans({ history }) {
    const [File, setFile] = useState(null);
    const [Base64, setBase64] = useState([]); // 파일 base64
    const handleChangeFile = (event) => {

        console.log(event.target.files)
        setFile(event.target.files);
        //fd.append("file", event.target.files)
        setBase64([]); //이거 미리보기
        for (var i = 0; i < event.target.files.length; i++) {
            if (event.target.files[i]) {
                let reader = new FileReader();
                reader.readAsDataURL(event.target.files[i]); // 1. 파일을 읽어 버퍼에 저장합니다.
                // 파일 상태 업데이트
                reader.onloadend = () => {
                    // 2. 읽기가 완료되면 아래코드가 실행됩니다.
                    const base64 = reader.result;
                    console.log(base64)
                    if (base64) {
                        //  images.push(base64.toString())
                        var base64Sub = base64.toString()

                        setBase64(imgBase64 => [...imgBase64, base64Sub]);
                        //  setImgBase64(newObj);
                        // 파일 base64 상태 업데이트
                        //  console.log(images)
                    }
                }
            }
        }

    }
    return (
        <contents>
            <p>PDF 파일 첨부</p>
            <input type="file" id="file" onChange={handleChangeFile} accept=".pdf" />

            <button
                onClick={() => { history.push("/result") }}
                style={{
                    margin: '20px',
                    width: '80px'
                }}>확인</button>

        </contents>

    );

}

export default Braille_PDF_trans;