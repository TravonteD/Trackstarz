import React from 'react'
import Header from './Header.js'
import ProfileLeft from './ProfileLeft.js'
import ProfileRight from './ProfileRight.js'
import Hero from './Hero.js'
import Feed from './Feed.js'

function Home() {
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

export default Home;
