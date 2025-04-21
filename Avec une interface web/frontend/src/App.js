import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Sidebar from './Composant/Sidebar';
import Potatos from './Potatos';
import Entrainement from './Entrainement';
import Tomatos from './Tomatos';
import Mais from './Mais';
import Ble from './Ble';
import Riz from './Riz';
import Arachid_riz from './Arachid_riz';
import DataPlants from './DataPlants';
import WebsiteData from './WebsiteData';
import QualiteDonnees from './QualiteDonnees';


function App() {
  return (
    <div className="flex h-screen">
      <Sidebar />
      <div className="flex-grow overflow-y-auto ">
        <Routes>
          <Route path="/" element={<Navigate to="/Entrainement" replace />} />
          <Route path="/Entrainement" element={<Entrainement />} />
          <Route path="/Potatos" element={<Potatos />} />
          <Route path="/Tomate" element={<Tomatos />} />
          <Route path="/Mais" element={<Mais />} />
          <Route path="/Ble" element={<Ble />} />
          <Route path="/Riz" element={<Riz />} />
          <Route path="/Arachid_riz" element={<Arachid_riz />} />
          <Route path="/DataPlants" element={<DataPlants />} />
          <Route path="/WebsiteData" element={<WebsiteData />} />
          <Route path="/QualiteDonnees" element={<QualiteDonnees/>} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
