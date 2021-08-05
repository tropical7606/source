import React from 'react';
import styled from "styled-components";

const Braille_PDF_result=(props) => {
    return (
        <div>
            <p>번역 결과 </p>
            <br/>
            <button style={{
                margin: '20px'
            }}>오역 확인</button>
            <button
            style={{
                margin: '20px'}}>추천단어</button>
        </div>
    );
}
export default Braille_PDF_result;