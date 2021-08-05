import React from 'react';

const Braille_ServiceCent=(props) => {
    return (
        <div style={{margin : "20px"}}>
            <h1>고객 센터 MENU</h1>
            <button
             style={{
                marginTop:"50px",
                width:"500px",
                height : "130px",
                fontSize : "30pt"
            }}>Q & A</button><br/>
            <button
             style={{
                marginTop:"50px",
                width:"500px",
                height : "130px",
                fontSize : "30pt"
            }}>오역, 오염 문제 건의</button><br/>
            <button
             style={{
                marginTop:"50px",
                width:"500px",
                height : "130px",
                fontSize : "30pt"
            }}>추천 문구 오류 문제 건의</button><br/>
            
        </div>
    );
}
export default Braille_ServiceCent;