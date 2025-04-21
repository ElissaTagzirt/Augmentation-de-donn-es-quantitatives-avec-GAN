
import React, { useState , useEffect } from 'react';


const QualiteDonnees = () => {
    const [paramtre,setparamtre]=useState('');
    const [culture,setculture]=useState('');
    const[QualiteDesDonneesGenere,setQualiteDesDonneesGenere]=useState(false);

    return (
        <div>
             <div className="flex items-center mb-4 mt-6 pl-8">
                    <p className="text-3xl font-medium mt-5 leading-none text-teal-500 ">
                        Qualité des données générées 
                        </p>
                    
                    </div>

      <div className="flex w-full  m-4 flex-col">
                    
          <form>

                    <div className="flex py-2">
           
                    

                    <div className='flex'> 
                <div className="flex items-center my-4 pl-4">
                  <p className="text-lg font-medium mt-5 ml-4  mr-3 leading-none text-gray-500 ">
                  Indiquez la culture selon laquelle vous voulez effectuer une comparaison : 
                    </p>
                </div>
                <div className="w-1/2 m-2 items-center border-b border-teal-500 py-4 px-2">
                <select
                        className="appearance-none bg-transparent border border-gray-300 w-full text-gray-700 py-1 px-2 leading-tight focus:outline-none"
                        value={culture}
                        onChange={(e) => setculture(e.target.value)}
                    >
                        <option value="">Sélectionnez une culture</option>
                       
                        <option  value="arachides_riz">Arachides_riz</option>
                        <option  value="ble">Blé</option>
                        <option  value="data_plants">Plantes</option>
                        <option  value="mais">Mais</option>
                        <option  value="potato">Potato</option>
                        <option  value="riz">Riz</option>
                        <option  value="tomates">Tomates</option>
                        <option  value="website">Website</option>
                    
                    </select>
                </div>


                </div>
              <div className='flex'> 
                <div className="flex items-center my-4 pl-4">
                  <p className="text-lg font-medium mt-5 ml-4  mr-3 leading-none text-gray-500 ">
                  Indiquez le paramètre selon lequel la comparaison des données sera effectuée : 
                    </p>
                </div>
                <div className="w-1/2 m-2 items-center border-b border-teal-500 py-4 px-2">
                    <input
                        type="text"
                        placeholder="paramètre"
                        className="appearance-none bg-transparent border-none w-full text-gray-700 py-1 px-2 leading-tight focus:outline-none"
                        value={paramtre}
                        onChange={(e) => setparamtre(e.target.value)}
                    />
                </div>


                </div>




                <div className="w-1/5 m-5 justify-end">
                    <button
                     onClick={() => {
                      setQualiteDesDonneesGenere(true)
                     }}
                    type="button"
                    className="px-4 py-2 bg-teal-500 hover:bg-teal-700 text-white font-bold rounded">
                Afficher les graphes </button>
                </div>    
            </div>
           </form>

            {QualiteDesDonneesGenere &&  (
                 <div className="overflow-x-auto mt-4">
                 <div className="inline-block min-w-full py-2 px-4 sm:px-6 lg:px-8">
                    <div className="flex items-center my-4 pl-4">
                        <p className="text-2xl font-medium mt-5 ml-4  mr-3 leading-none text-teal-700 ">
                             Histogramme : 
                        </p>
                    </div>
                    <div>
                        <img src={`${process.env.PUBLIC_URL}/Image_genere/${culture}histo_month_${paramtre}.png`} alt="Potato boxplot" />
                    </div>
                 </div>
                 <div className="inline-block min-w-full py-2 px-4 sm:px-6 lg:px-8">
                    <div className="flex items-center my-4 pl-4">
                        <p className="text-2xl font-medium mt-5 ml-4  mr-3 leading-none text-teal-700 ">
                              Fréquences cumulées : 
                        </p>
                    </div>
                    <div> 
                        <img src={`${process.env.PUBLIC_URL}/Image_genere/${culture}cumulative_${paramtre}.png`} alt="Potato boxplot" />
                    </div>
                 </div>
                 <div className="inline-block min-w-full py-2 px-4 sm:px-6 lg:px-8">
                    <div className="flex items-center my-4 pl-4">
                        <p className="text-2xl font-medium mt-5 ml-4  mr-3 leading-none text-teal-700 ">
                              Boite à moustache : 
                        </p>
                    </div>
                    <div> 
                        <img src={`${process.env.PUBLIC_URL}/Image_genere/${culture}boxplot_${paramtre}.png`} alt="Potato boxplot" />
                    </div>
                 </div>
             </div>
            )}
        </div>


        </div>
    );
};

export default QualiteDonnees;
