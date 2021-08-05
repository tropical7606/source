import React from 'react';
import styled from "styled-components";

const Braille_Main = ({history}) => {
    return (
        <div>
            <programName>
                <h1>점자 번역 프로그램</h1>

            </programName>
            <button
                onClick={()=>{history.push("/PDFtrans")}}
                style={{
                    width: '250px',
                    height: '30px',
                    backgroundColor: '#eee',
                    margin: '100px'
                }} >PDF 파일 번역</button>
            <button
                 onClick={()=>{history.push("/TextTrans")}}
                style={{
                    width: '250px',
                    height: '30px',
                    backgroundColor: '#eee',
                    margin: '100px'
                }}>직접 번역</button>
            <As>
                <p
                    style={{
                        textAlign: 'center',
                        fontSize: '8pt'
                    }}
                    onClick ={()=>{history.push("/serviceCent")}}>고객센터</p>
            </As>
        </div>
    );
}


const programName = styled.div`
display: flex;
flex-direction: column;
height: 100%;
width:250px;
overflow-x: hidden;
overflow-y: auto;
`;

const As = styled.div`
position: absolute;
width:100%;
height : 5%;
`; 

export default Braille_Main;