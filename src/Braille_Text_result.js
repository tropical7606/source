import React from 'react';

const Braille_Text_result=({history})=>{
    return (
        <div>
            <h3 style={{
                color :"#333366"
            }}>변환 결과</h3>
            

            <input type="text" 
                style = {{width : "500px",
                        height:"200px"}}></input>
            <br/>
            <button
                 style={{marginTop:"30px",width : "50px"}}
                 onClick={()=>{history.push("/")}}>확인</button>
        </div>
    );
}
export default Braille_Text_result;