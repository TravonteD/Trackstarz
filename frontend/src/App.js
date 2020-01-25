import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <Header/>
    </div>
  );
}

class Header extends React.Component {
  render() {
    return (
      <header className="trackstarz__header">
      <Menu/>
      </header>
    )
  }
}

class Menu extends React.Component {
  render() {
    return (
      <nav className="trackstarz__header__nav">
        <li className="trackstarz__header_nav_item">Home</li>
        <li>About</li>
        <li>Universe</li>
      </nav>
    )
  }
}

export default App;
