import React from 'react';
import Header from './components/Header.js'
import ProfileLeft from './components/ProfileLeft.js'
import ProfileRight from './components/ProfileRight.js'
import Hero from './components/Hero.js'
import Feed from './components/Feed.js'
import './App.css';

function App() {
  return (
    <div className="app">
      <Header/>
      <Hero/>
      <div className='container app__content'>
        <div className='row'>
          <ProfileLeft/>
          <Feed/>
          <ProfileRight/>
        </div>
      </div>
    </div>
  )
}

export default App;
