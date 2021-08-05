import logo from './logo.svg';
import './App.css';
import Braille_PDF_trans from './Braille_PDF_trans';
import Braille_Main from './Braille_Main.js';
import Braille_Text_trans from './Braille_Text_trans';
import Braille_PDF_result from './Braille_PDF_result';
import Braille_Text_result from './Braille_Text_result';
import Braille_ServiceCent from './Braille_ServiceCent';
import React, { Component } from 'react';
import { BrowserRouter, Route } from "react-router-dom";

//as는 별명 지정 

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
        
    }
  }

  render() {
    return (
      <div className='App'>

        <BrowserRouter>
          <Route path="/" exact component={Braille_Main}/>
          <Route path="/PDFtrans" component={Braille_PDF_trans} />
          <Route path="/result" component={Braille_PDF_result}/>
          <Route path="/TextTrans" component={Braille_Text_trans}/>
          <Route path="/Textresult" component={Braille_Text_result}/>
          <Route path="/serviceCent" component={Braille_ServiceCent}/>
        </BrowserRouter>

        
      </div>
    );
  }
}




export default App;
