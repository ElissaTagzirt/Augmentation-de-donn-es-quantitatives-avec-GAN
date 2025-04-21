import React, { useState , useEffect } from 'react';
import { Link } from 'react-router-dom';
import "../index.css"

const Sidebar = () => {

  

  const handleLogout = () => {
    
  };
  return (
    <div className="h-screen flex flex-col text-gray-800">

     <div className="w-50 sm:w-60 flex flex-col top-0 left-0 bg-white min-h-screen border-r ">


        <div className="flex items-center ml-6 h-14 border-b">
           <div className="flex m-3">
            <h5 style={{ color: '#52B8B5' }} className="ml-3 text-lg font-semibold">Agriculture</h5>
            </div>
        </div>
        <div className=" flex-grow">
          <ul className="flex flex-col py-2 space-y-1">

          <li className="px-5">
              <div className="flex flex-row items-center h-8">
              <div className="text-sm font-light tracking-wide text-gray-500 w-48">GAN</div>

              </div>
            </li>
            
            <li>
              <Link  to="/Entrainement" className="relative flex flex-row items-center h-11 focus:outline-none hover:bg-gray-50 text-gray-600 hover:text-gray-800 border-l-4 border-transparent hover:border-[#52B8B5] pr-6">
                <span className="inline-flex justify-center items-center ml-4">
                </span>
                <span className="ml-2 text-sm tracking-wide truncate">Entraînement du GAN</span>
              </Link>
            </li>
            <li className="px-5">
              <div className="flex flex-row items-center h-8">
              <div className="text-sm font-light tracking-wide text-gray-500 w-48">Monoculture</div>

              </div>
            </li>
            
            <li>
              <Link  to="/Potatos" className="relative flex flex-row items-center h-11 focus:outline-none hover:bg-gray-50 text-gray-600 hover:text-gray-800 border-l-4 border-transparent hover:border-[#52B8B5] pr-6">
                <span className="inline-flex justify-center items-center ml-4">
                </span>
                <span className="ml-2 text-sm tracking-wide truncate">Pomme de terre</span>
              </Link>
            </li>
            <li>
              <Link  to="/Tomate" className="relative flex flex-row items-center h-11 focus:outline-none hover:bg-gray-50 text-gray-600 hover:text-gray-800 border-l-4 border-transparent hover:border-[#52B8B5] pr-6">
                <span className="inline-flex justify-center items-center ml-4">
                
              </span>
                <span className="ml-2 text-sm tracking-wide truncate">Tomate</span>
               
              </Link>
            </li>
            <li>
              <Link to="/Mais" className="relative flex flex-row items-center h-11 focus:outline-none hover:bg-gray-50 text-gray-600 hover:text-gray-800 border-l-4 border-transparent hover:border-[#52B8B5] pr-6">
                <span className="inline-flex justify-center items-center ml-4">
                  
                </span>
                <span className="ml-2 text-sm tracking-wide truncate">Mais</span>
              </Link>
            </li>
            <li>
              <Link  to="/Ble" className="relative flex flex-row items-center h-11 focus:outline-none hover:bg-gray-50 text-gray-600 hover:text-gray-800 border-l-4 border-transparent hover:border-[#52B8B5] pr-6">
                <span className="inline-flex justify-center items-center ml-4">
                
              </span>
                <span className="ml-2 text-sm tracking-wide truncate">Blé</span>
               
              </Link>
            </li> 
            <li>
            <Link  to="/Riz" className="relative flex flex-row items-center h-11 focus:outline-none hover:bg-gray-50 text-gray-600 hover:text-gray-800 border-l-4 border-transparent hover:border-[#52B8B5] pr-6">
            <span className="inline-flex justify-center items-center ml-4">
                  
                
              </span>
              <span className="ml-2 text-sm tracking-wide truncate">Riz</span>
            </Link>
            </li>
            
            <li className="px-5">
              <div className="flex flex-row items-center h-8">

                    <div className="text-sm font-light tracking-wide text-gray-500">Polyculture</div>
                  </div>
                </li>

                <li>
            <Link  to="/Arachid_riz" className="relative flex flex-row items-center h-11 focus:outline-none hover:bg-gray-50 text-gray-600 hover:text-gray-800 border-l-4 border-transparent hover:border-[#52B8B5] pr-6">
            <span className="inline-flex justify-center items-center ml-4">
            
            </span>

                <span className="ml-2 text-sm tracking-wide truncate">Archides et riz</span>
              </Link>
            </li>
              
                <li>
                  <Link to="/DataPlants" className="relative flex flex-row items-center h-11 focus:outline-none hover:bg-gray-50 text-gray-600 hover:text-gray-800 border-l-4 border-transparent hover:border-[#52B8B5] pr-6">
                    <span className="inline-flex justify-center items-center ml-4">
                    

                    </span>
                    <span className="ml-2 text-sm tracking-wide truncate">Data plants</span>
                    
                  </Link>
                </li>
                <li>
                  <Link to="/WebsiteData" className="relative flex flex-row items-center h-11 focus:outline-none hover:bg-gray-50 text-gray-600 hover:text-gray-800 border-l-4 border-transparent hover:border-[#52B8B5] pr-6">
                    <span className="inline-flex justify-center items-center ml-4">
                   

                    </span>
                    <span className="ml-2 text-sm tracking-wide truncate">Web site data</span>
                    
                  </Link>
                </li>

              {/*   <li>
                  <Link to="/QualiteDonnees" className="relative flex flex-row items-center h-11 focus:outline-none hover:bg-gray-50 text-gray-600 hover:text-gray-800 border-l-4 border-transparent hover:border-[#52B8B5] pr-6">
                    <span className="inline-flex justify-center items-center ml-4">
                   

                    </span>
                    <span className="ml-2 text-sm tracking-wide truncate">Qualité des données</span>
                    
                  </Link>
  </li> */}
              
             
              </ul>
            </div>
          </div>
     </div>
    );
};

export default Sidebar;