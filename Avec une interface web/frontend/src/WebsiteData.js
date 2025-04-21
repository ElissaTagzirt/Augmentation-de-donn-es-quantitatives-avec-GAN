import React, { useState , useEffect } from 'react';
    

function WebsiteData() {
   
    
    const [Nbligne,setNbligne]=useState(0);
    const [deuxpartie,setdeuxpartie]=useState(false);
    const [Affichedonnebrute , setAffichedonnebrute]=useState(false);
    const [Affichedonnegenere, setAffichedonnegenere]=useState(false);
    const [QualiteDesDonneesGenere, setQualiteDesDonneesGenere]=useState(false);
    const [paramtre,setparamtre]=useState('');
    const [donnees, setDonnees] = useState([]);
    const [donneesGenere, setDonneesGenere] = useState([]);
    const [entete , setentete]=useState([]);

    const chargerDonnees = async () => {
        try {
            const reponse = await fetch('http://127.0.0.1:8000/websitedata/donneBrute');
            if (reponse.ok) {
                const texte = await reponse.text();
                const lignes = texte.split('\n');
                const entetes = lignes[0].split(',');
                const donnees = lignes.slice(1).map(ligne => ligne.split(',').reduce((acc, val, index) => {
                    acc[entetes[index]] = val;
                    return acc;
                }, {}));
                setDonnees(donnees);
                //setentete(entetes);
                console.log(donnees);
            } else {
                console.error('Erreur lors du chargement des données:', reponse.statusText);
            }
        } catch (error) {
            console.error('Erreur de réseau:', error);
        }
    };

    const chargerDonneesCommparative = async () => {
        try {
            const reponse = await fetch('http://127.0.0.1:8000/websitedata/comparative');
            if (reponse.ok) {
                const texte = await reponse.text();
                const lignes = texte.split('\n');
                const entetes = lignes[0].split(',');
                const donnees = lignes.slice(1).map(ligne => ligne.split(',').reduce((acc, val, index) => {
                    acc[entetes[index]] = val;
                    return acc;
                }, {}));
                setentete(entetes);
            } else {
                console.error('Erreur lors du chargement des données:', reponse.statusText);
            }
        } catch (error) {
            console.error('Erreur de réseau:', error);
        }
    };
    const chargerDonneesGenere = async (event) => {
        event.preventDefault();
        try {
            const reponse = await fetch('http://127.0.0.1:8000/websitedata/donneGenere');
            if (reponse.ok) {
                const texte = await reponse.text();
                const lignes = texte.split('\n');
                const entetes = lignes[0].split(',');
                const donnees = lignes.slice(1).map(ligne => ligne.split(',').reduce((acc, val, index) => {
                    acc[entetes[index]] = val;
                    return acc;
                }, {}));
                setDonneesGenere(donnees);
                console.log(donnees);
            } else {
                console.error('Erreur lors du chargement des données:', reponse.statusText);
            }
        } catch (error) {
            console.error('Erreur de réseau:', error);
        }
    };
    

    useEffect(() => {
        // Appeler la fonction pour charger les données lors du montage du composant
        chargerDonnees();
        chargerDonneesCommparative();
    }, []);
   

    const handlelancelagenreation = async () => {
        try {
            const response = await fetch('http://127.0.0.1:8000/websitedata/genere', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    nb_lignes_generees: Nbligne // Inclure la valeur de Nbligne dans le corps de la requête JSON
                })
            });
    
            if (response.ok) {
                console.log('Succès:', response);
                setdeuxpartie(true);
            } else {
                console.error('Erreur:', response.statusText);
            }
        } catch (error) {
            console.error('Erreur lors de l\'appel à l\'API:', error);
            // Gérez l'erreur ici si nécessaire
        }
    };

      return (
    
        
    <div>
       <div className="flex items-center my-8 pl-8">
               <p className="text-4xl font-medium mt-5 leading-none text-teal-500 mr-2">Augmentation de données pour le fichier Website Data</p>
            </div> 
            
            
     {!deuxpartie ? ( <div   >  
            

            <div className="mx-4 ">
                <form>
                <div className="flex items-center my-8 pl-4">
               <p className="text-xl font-medium mt-5 leading-none text-teal-500 ">
               Génération de nouvelles lignes de données :
               </p>
            </div>
                
            <div className="flex py-2">
           
              <div className='flex'> 
                <div className="flex items-center my-4 pl-4">
                  <p className="text-lg font-medium mt-5 ml-4  mr-3 leading-none text-gray-500 ">
                  Indiquez le nombre de lignes de données à générer : 
                    </p>
                </div>
                <div className="w-1/2 m-2 items-center border-b border-teal-500 py-4 px-2">
                    <input
                        type="number"
                        placeholder="nombre de ligne"
                        className="appearance-none bg-transparent border-none w-full text-gray-700 py-1 px-2 leading-tight focus:outline-none"
                        value={Nbligne}
                        onChange={(e) => setNbligne(parseInt(e.target.value))}
                    />
                </div>

                </div> 
                
    
            

            
                <div className="w-1/5 m-5 items-center ">
                    <button
                    onClick={(e) => {
                        e.preventDefault();
                        handlelancelagenreation(e);
                    }}
                    type="button"
                className="flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded">
                Lancer la géneration </button>
                </div>    
            </div>
           
                </form>
            </div>
                

            <div className="flex w-full flex-col">
                <div className="my-8 pl-8">
                        <p className="text-lg font-medium leading-none text-gray-500">
                            Les données initiales :
                        </p>
                    </div>
                    <div className="flex justify-end mr-10 pr-8">
                        <button
                            onClick={() => setAffichedonnebrute(!Affichedonnebrute)}
                            className="px-4 py-2 bg-teal-500 hover:bg-teal-700 text-white font-bold rounded">
                            Affiche données
                        </button>
                    </div>

                    {Affichedonnebrute && (
                <div className="overflow-x-auto mt-4">
                    <div className="inline-block min-w-full py-2 px-4 sm:px-6 lg:px-8">
                        <div className="overflow-hidden">
                            <table className="w-full text-center text-sm font-light">
                                <thead className="border-b bg-teal-500 font-medium text-white">
                                    <tr>
                                    <th scope="col" className="px-6 py-4">N°</th>
                                    <th scope="col" className="px-6 py-4">Crop</th>
                                    <th scope="col" className="px-6 py-4">Total growing period (days)</th>
                                    <th scope="col" className="px-6 py-4">Crop water need (mm/total growing period)</th>
                              </tr>
                          </thead>
                          <tbody>

                          {donnees.slice(0, -1).map((ligne, index) => ( // Utiliser slice pour exclure le dernier élément
                              <tr key={index} className="border-b dark:border-neutral-500 focus:outline-none border border-gray-100 rounded">
                                  <td className="whitespace-nowrap px-6 py-4 ">{index + 1}</td>
                                  {Object.values(ligne).map((valeur, indexValeur) => (
                                      <td key={indexValeur} className="px-6 py-4">{valeur}</td>
                                  ))}
                              </tr>
                          ))}
                          </tbody>
                      </table>
                  </div>
              </div>
          </div>
      )}
        </div>


    
         
     </div> ): (<div className='ml-4'>
                  <div className="flex items-center my-8 pl-4">
                    <p className="text-lg font-medium m-5 leading-none text-gray-500 ">
                    Le nombre de lignes de données générées   <span className='text-lg font-medium m-5 leading-none text-teal-500'>{Nbligne}</span>
                       </p>
                    </div>
                    

  <div className="flex w-full flex-col">

    
     
        <div className="flex w-full flex-col">

            
        <div className="flex w-full flex-col">
                <div className="my-8 pl-8">
                <p className="text-3xl font-medium mt-5 leading-none text-teal-500 ">
                      Les données initiales :
                        </p>
                    </div>
                    <div className="flex justify-end mr-10 pr-8">
                        <button
                            onClick={() => setAffichedonnebrute(!Affichedonnebrute)}
                            className="px-4 py-2 bg-teal-500 hover:bg-teal-700 text-white font-bold rounded">
                            Afficher données
                        </button>
                    </div>

                    {Affichedonnebrute && (
                <div className="overflow-x-auto mt-4">
                    <div className="inline-block min-w-full py-2 px-4 sm:px-6 lg:px-8">
                        <div className="overflow-hidden">
                            <table className="w-full text-center text-sm font-light">
                                <thead className="border-b bg-teal-500 font-medium text-white">
                                    <tr>
                                    <th scope="col" className="px-6 py-4">N°</th>
                                    <th scope="col" className="px-6 py-4">Crop</th>
                                    <th scope="col" className="px-6 py-4">Total growing period (days)</th>
                                    <th scope="col" className="px-6 py-4">Crop water need (mm/total growing period)</th>
                              </tr>
                          </thead>
                          <tbody>

                          {donnees.slice(0, -1).map((ligne, index) => ( // Utiliser slice pour exclure le dernier élément
                              <tr key={index} className="border-b dark:border-neutral-500 focus:outline-none border border-gray-100 rounded">
                                  <td className="whitespace-nowrap px-6 py-4 ">{index + 1}</td>
                                  {Object.values(ligne).map((valeur, indexValeur) => (
                                      <td key={indexValeur} className="px-6 py-4">{valeur}</td>
                                  ))}
                              </tr>
                          ))}
                          </tbody>
                      </table>
                  </div>
              </div>
          </div>
      )}
  </div>
<div className="flex w-full flex-col">
          <div className="my-8 pl-8">
                  <p className="text-3xl font-medium mt-5 leading-none text-teal-500 ">
                      Les données générées avec le GAN :
                  </p>
              </div>
              <div className="flex justify-end mr-10 pr-8">
                  <button
                      onClick={(e) => {
                          e.preventDefault(); 
                          chargerDonneesGenere(e);
                          setAffichedonnegenere(!Affichedonnegenere)}}
                      className="px-4 py-2 bg-teal-500 hover:bg-teal-700 text-white font-bold rounded">
                      Affiche données
                  </button>

                  
              </div>

      {Affichedonnegenere &&  (
          <div className="overflow-x-auto mt-4">
              <div className="inline-block min-w-full py-2 px-4 sm:px-6 lg:px-8">
                  <div className="overflow-hidden">
                      <table className="w-full text-center text-sm font-light">
                          <thead className="border-b bg-teal-500 font-medium text-white">
                              <tr>
                              <th scope="col" className="px-6 py-4">N°</th>
                              <th scope="col" className="px-6 py-4">Crop</th>
                              <th scope="col" className="px-6 py-4">Total growing period (days)</th>
                              <th scope="col" className="px-6 py-4">Crop water need (mm/total growing period)</th>
                              </tr>
                          </thead>
                          <tbody>

                          {donneesGenere.slice(0, -1).map((ligne, index) => ( // Utiliser slice pour exclure le dernier élément
                              <tr key={index} className="border-b dark:border-neutral-500 focus:outline-none border border-gray-100 rounded">
                                  <td className="whitespace-nowrap px-6 py-4 ">{index + 1}</td>
                                  {Object.values(ligne).map((valeur, indexValeur) => (
                                      <td key={indexValeur} className="px-6 py-4">{valeur}</td>
                                  ))}
                              </tr>
                          ))}
                          </tbody>
                      </table>
                  </div>
              </div>
          </div>
      )}
  </div>  

     </div>  
      
   {/* <div className="flex items-center mb-4 mt-6 pl-8">
                    <p className="text-3xl font-medium mt-5 leading-none text-teal-500 ">
                        Qualité des données générées 
                        </p>
                    
                    </div>

      <div className="flex w-full  m-4 flex-col">
                    


                    <div className="flex py-2">
           
              <div className='flex'> 
                <div className="flex items-center my-4 pl-4">
                  <p className="text-lg font-medium mt-5 ml-4  mr-3 leading-none text-gray-500 ">
                  Indique le paramètre selon lequel la comparaison des données sera effectuée : 
                    </p>
                </div>
                <div className="w-1/2 m-2 items-center border-b border-teal-500 py-4 px-2">
                <div className="overflow-hidden">
                <select
                        className="appearance-none bg-transparent border border-gray-300 w-full text-gray-700 py-1 px-2 leading-tight focus:outline-none"
                        value={paramtre}
                        onChange={(e) => setparamtre(e.target.value)}
                    >
                        <option value="">Sélectionnez un paramètre</option>
                       
                        <option  value="Crop_water_need_mm">Crop_water_need_mm</option>
                        <option  value="Growing_period_days">Growing_period_days</option>
                    
                    </select>
                    </div>
                </div>
                </div> 
                <div className="w-1/5 m-5 justify-end">
                    <button
                     onClick={() => {setQualiteDesDonneesGenere(!setQualiteDesDonneesGenere)}}
                    type="button"
                    className="px-4 py-2 bg-teal-500 hover:bg-teal-700 text-white font-bold rounded">
                Afficher les graphes </button>
                </div>    
            </div>

            {QualiteDesDonneesGenere &&  (
                 <div className="overflow-x-auto mt-4">
                 <div className="inline-block min-w-full py-2 px-4 sm:px-6 lg:px-8">
                    <div className="flex items-center my-4 pl-4">
                        <p className="text-2xl font-medium mt-5 ml-4  mr-3 leading-none text-teal-700 ">
                             Histogramme : 
                        </p>
                    </div>
                    <div>
                        <img src={`${process.env.PUBLIC_URL}/Image_genere/websitehisto_month_${paramtre}.png`} alt="Website Histogramme" />
                    </div>
                 </div>
                 <div className="inline-block min-w-full py-2 px-4 sm:px-6 lg:px-8">
                    <div className="flex items-center my-4 pl-4">
                        <p className="text-2xl font-medium mt-5 ml-4  mr-3 leading-none text-teal-700 ">
                              Fréquences cumulées : 
                        </p>
                    </div>
                    <div> 
                        <img src={`${process.env.PUBLIC_URL}/Image_genere/websitecumulative_${paramtre}.png`} alt="Website cumulative" />
                    </div>
                 </div>
                 <div className="inline-block min-w-full py-2 px-4 sm:px-6 lg:px-8">
                    <div className="flex items-center my-4 pl-4">
                        <p className="text-2xl font-medium mt-5 ml-4  mr-3 leading-none text-teal-700 ">
                              Boite à moustache : 
                        </p>
                    </div>
                    <div> 
                        <img src={`${process.env.PUBLIC_URL}/Image_genere/websiteboxplot_${paramtre}.png`} alt="Website boxplot" />
                    </div>
                 </div>
             </div>
            )}
        </div>  */}

                <div className="flex justify-end my-10 mr-12 pr-8 ">
                
                
                <button
                onClick={() => setdeuxpartie(!deuxpartie)}
                className="px-4 py-2 bg-teal-500 hover:bg-teal-700 text-white font-bold rounded">
                    Générer de nouvelles données
                </button>
                {!deuxpartie && (<button
                className="m-4 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded" type="submit">
                    Valider
                </button>
                
                )}
                
                
                </div>
           </div> 


     </div>)}      
    </div> 
    
      );
    }


export default WebsiteData;
