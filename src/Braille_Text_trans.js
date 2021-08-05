import React from 'react';
import styled from "styled-components";
const Braille_Text_trans=({history})=>{
    return (
        <div>
            <h3>한글 입력</h3>
            <input type="text" 
                style = {{width : "500px",
                        height:"200px"}}></input>
            <br/>
            <button
                style={{marginTop:"30px"}} 
                onClick={()=>{history.push("/Textresult")}}>점자 변환하기</button>
           
        </div>
    );
}
export default Braille_Text_trans;