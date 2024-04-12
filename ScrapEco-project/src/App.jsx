import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Hero from "./components/Hero";
import "./App.css";
import Header from "./components/Header";
import Login from "./components/Login";
//import Hero from "./components/Hero";

function App() {
  return (
    <div className="App">
      <Header/>
      <Hero/>
      <Router>
        <Routes>
          <Route exact path="/" element={<Login/>}></Route>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
