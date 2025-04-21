import React, { useState , useEffect } from 'react';
    

function Entrainement() {
   
   // lancement de la donne vers le backend 
    const [NbiterartionPotatos,setNbiterartionPotatos]=useState(0);
    const [NbiterartionTomatos,setNbiterartionTomatos]=useState(0);
    const [NbiterartionMais,setNbiterartionMais]=useState(0);
    const [NbiterartionBle,setNbiterartionBle]=useState(0);
    const [NbiterartionRiz,setNbiterartionRiz]=useState(0);
    const [NbiterartionArachid_riz,setNbiterartionArachid_riz]=useState(0);
    const [NbiterartionDataPlants,setNbiterartionDataPlants]=useState(0);
    const [NbiterartionWebsitePlants,setNbiterartionWebsitePlants]=useState(0);
    
    // la response genre de backend par rapport a l'entrainement 
    const [ReponsePotatos,setReponsePotatos]=useState('');
    const [ReponseTomatos,setReponseTomatos]=useState('');
    const [ReponseMais,setReponseMais]=useState('');
    const [ReponseBle,setReponseBle]=useState('');
    const [ReponseRiz,setReponseRiz]=useState('');
    const [ReponseArachid_riz,setReponseArachid_riz]=useState('');
    const [ReponseDataPlants,setReponseDataPlants]=useState('');
    const [ReponseWebsitePlants,setReponseWebsitePlants]=useState('');
    

     
    // fonction de lancememnt de backend  

    const handlelancerEntraianementpotatos = async (event) => {
        event.preventDefault();
        try {
            
            const response = await fetch('http://127.0.0.1:8000/potato/entraianement', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    nb_entrainement: NbiterartionPotatos,
                }),
            });
    
            if (response.ok) {
                const data = await response.json();
                console.log('Entraînement lancé avec succès:', data);
                setReponsePotatos("Entraînement terminé avec succès.");
                
            } else {
                console.error('Erreur lors de la tentative de lancement de l\'entraînement:', response.statusText);
                setReponsePotatos("Erreur lors de la tentative de lancement de l\'entraînement:'");
            }
        } catch (error) {
            console.error('Erreur lors de l\'appel au backend:', error);
            // Gérez ici les erreurs de réseau ou autres erreurs inattendues
        }
    };
    
    const handlelancerEntraianementTomatos = async (event) => {
        event.preventDefault();
        try {
            const response = await fetch('http://127.0.0.1:8000/tomates/entraianement', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    nb_entrainement: NbiterartionTomatos,
                }),
            });
    
            if (response.ok) {
                const data = await response.json();
                console.log('Entraînement lancé avec succès:', data);
                setReponseTomatos("Entraînement terminé avec succès.");
                
            } else {
                console.error('Erreur lors de la tentative de lancement de l\'entraînement:', response.statusText);
                setReponseTomatos("Erreur lors de la tentative de lancement de l\'entraînement:'");
            }
        } catch (error) {
            console.error('Erreur lors de l\'appel au backend:', error);
            // Gérez ici les erreurs de réseau ou autres erreurs inattendues
        }
    };
      

    const handlelancerEntraianementMais = async (event) => {
        event.preventDefault();
        try {
            const response = await fetch('http://127.0.0.1:8000/mais/entraianement', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    nb_entrainement: NbiterartionMais,
                }),
            });
    
            if (response.ok) {
                const data = await response.json();
                console.log('Entraînement lancé avec succès:', data);
                setReponseMais("Entraînement terminé avec succès.");
                
            } else {
                console.error('Erreur lors de la tentative de lancement de l\'entraînement:', response.statusText);
                setReponseMais("Erreur lors de la tentative de lancement de l\'entraînement:'");
            }
        } catch (error) {
            console.error('Erreur lors de l\'appel au backend:', error);
            // Gérez ici les erreurs de réseau ou autres erreurs inattendues
        }
    };
      
    const handlelancerEntraianementBle = async (event) => {
        event.preventDefault();
        try {
            const response = await fetch('http://127.0.0.1:8000/ble/entraianement', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    nb_entrainement: NbiterartionBle,
                }),
            });
    
            if (response.ok) {
                const data = await response.json();
                console.log('Entraînement lancé avec succès:', data);
                setReponseBle("Entraînement terminé avec succès.");
                
            } else {
                console.error('Erreur lors de la tentative de lancement de l\'entraînement:', response.statusText);
                setReponseBle("Erreur lors de la tentative de lancement de l\'entraînement:'");
            }
        } catch (error) {
            console.error('Erreur lors de l\'appel au backend:', error);
            // Gérez ici les erreurs de réseau ou autres erreurs inattendues
        }
    };
      
    const handlelancerEntraianementRiz = async (event) => {
        event.preventDefault();
        try {
            const response = await fetch('http://127.0.0.1:8000/riz/entraianement', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    nb_entrainement: NbiterartionRiz,
                }),
            });
    
            if (response.ok) {
                const data = await response.json();
                console.log('Entraînement lancé avec succès:', data);
                setReponseRiz("Entraînement terminé avec succès.");
                
            } else {
                console.error('Erreur lors de la tentative de lancement de l\'entraînement:', response.statusText);
                setReponseRiz("Erreur lors de la tentative de lancement de l\'entraînement:'");
            }
        } catch (error) {
            console.error('Erreur lors de l\'appel au backend:', error);
            // Gérez ici les erreurs de réseau ou autres erreurs inattendues
        }
    };
      
    const handlelancerEntraianementArachid_riz = async (event) => {
        event.preventDefault();
        try {
            const response = await fetch('http://127.0.0.1:8000/arachides_riz/entrainement', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    nb_entrainement: NbiterartionArachid_riz,
                }),
            });
    
            if (response.ok) {
                const data = await response.json();
                console.log('Entraînement lancé avec succès:', data);
                setReponseArachid_riz("Entraînement terminé avec succès.");
                
            } else {
                console.error('Erreur lors de la tentative de lancement de l\'entraînement:', response.statusText);
                setReponseArachid_riz("Erreur lors de la tentative de lancement de l\'entraînement:'");
            }
        } catch (error) {
            console.error('Erreur lors de l\'appel au backend:', error);
            // Gérez ici les erreurs de réseau ou autres erreurs inattendues
        }
    };
      
    const handlelancerEntraianementDataPlants = async (event) => {
        event.preventDefault();
        try {
            const response = await fetch('http://127.0.0.1:8000/dataPalntes/entraianement', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    nb_entrainement: NbiterartionDataPlants,
                }),
            });
    
            if (response.ok) {
                const data = await response.json();
                console.log('Entraînement lancé avec succès:', data);
                setReponseDataPlants("Entraînement terminé avec succès.");
                
            } else {
                console.error('Erreur lors de la tentative de lancement de l\'entraînement:', response.statusText);
                setReponseDataPlants("Erreur lors de la tentative de lancement de l\'entraînement:'");
            }
        } catch (error) {
            console.error('Erreur lors de l\'appel au backend:', error);
            // Gérez ici les erreurs de réseau ou autres erreurs inattendues
        }
    };
      
    const handlelancerEntraianementWebsitePlants = async (event) => {
        event.preventDefault();
        try {
            const response = await fetch('http://127.0.0.1:8000/websitedata/entraianement', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    nb_entrainement: NbiterartionWebsitePlants,
                }),
            });
    
            if (response.ok) {
                const data = await response.json();
                console.log('Entraînement lancé avec succès:', data);
                setReponseWebsitePlants("Entraînement terminé avec succès.");
                
            } else {
                console.error('Erreur lors de la tentative de lancement de l\'entraînement:', response.statusText);
                setReponseWebsitePlants("Erreur lors de la tentative de lancement de l\'entraînement:'");
            }
        } catch (error) {
            console.error('Erreur lors de l\'appel au backend:', error);
            // Gérez ici les erreurs de réseau ou autres erreurs inattendues
        }
    };
      
        
        
       


    
    
   
    
      return (
    
        
    <div className="m-2 pb-4 w-full rounded shadow-lg">
       
            <div className="flex items-center my-8 pl-8">
               <p className="text-4xl font-medium mt-5 leading-none text-teal-500 mr-2">Entraînement des modules GAN dédiés à chaque fichier</p>
            </div>
            
    

            <div className="mx-4 ">
                <form>
                <div className="flex items-center my-8 pl-4">
               <p className="text-xl font-medium mt-5 leading-none text-teal-500 ">
               L'entraînement du module GAN pour le fichier Pomme de terre :</p>
            </div>
                
            <div className="flex py-2">
           
              <div className='flex'> 
                <div className="flex items-center my-4 pl-4">
                  <p className="text-lg font-medium mt-5 ml-4  mr-3 leading-none text-gray-500 ">
                  Indique le nombre d'itérations pour entraîner votre module :
                    </p>
                </div>
                <div className="w-1/2 m-2 items-center border-b border-teal-500 py-4 px-2">
                    <input
                        type="number"
                        placeholder="nombre d'itérations"
                        className="appearance-none bg-transparent border-none w-full text-gray-700 py-1 px-2 leading-tight focus:outline-none"
                        value={NbiterartionPotatos}
                        onChange={(e) => setNbiterartionPotatos(parseInt(e.target.value))} // Assurez-vous de convertir la valeur en entier avec parseInt
                    />
                </div>

                </div> 
                <div className="w-1/5 m-5 items-center ">
                    <button
                   
                    onClick={(e) => {
                        setReponsePotatos("Veuillez patienter jusqu'à la fin de l'entraînement du GAN.");
                        e.preventDefault(); // Empêche le rechargement de la page
                        handlelancerEntraianementpotatos(e); // Passez l'événement à la fonction
                    }}
                   
                    type="button"
                className="flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded">
                Lancer l'entraînement </button>
                </div>    
            </div>
            <div className="flex items-center my-8 pl-8">
                {ReponsePotatos && (
                    <div className="mr-4">
                        <p className={`text-lg font-medium ${ReponsePotatos.includes('succès') ? 'text-green-500' : 'text-red-500'}`}>
                            {ReponsePotatos}
                        </p>
                    </div>
                )}
               
            </div>
           
                </form>
            </div>

            <div className="mx-4 ">
                <form>
                <div className="flex items-center my-8 pl-4">
               <p className="text-xl font-medium mt-5 leading-none text-teal-500 ">
               L'entraînement du module GAN pour le fichier Tomates :</p>
            </div>
                
            <div className="flex py-2">
           
              <div className='flex'> 
                <div className="flex items-center my-4 pl-4">
                  <p className="text-lg font-medium mt-5 ml-4  mr-3 leading-none text-gray-500 ">
                  Indique le nombre d'itérations pour entraîner votre module :
                    </p>
                </div>
                <div className="w-1/2 m-2 items-center border-b border-teal-500 py-4 px-2">
                <input
                    type="number"
                    placeholder="nombre d'itérations"
                    className="appearance-none bg-transparent border-none w-full text-gray-700 py-1 px-2 leading-tight focus:outline-none"
                    value={NbiterartionTomatos} // Utilisation de la variable d'état correspondante
                    onChange={(e) => setNbiterartionTomatos(parseInt(e.target.value))} // Assurez-vous de convertir la valeur en entier avec parseInt
                />
            </div>

                </div> 

                <div className="w-1/5 m-5 items-center ">
                    <button
                     onClick={(e) => {
                        setReponseTomatos("Veuillez patienter jusqu'à la fin de l'entraînement du GAN.");
                        e.preventDefault();
                        handlelancerEntraianementTomatos(e);
                    }}
                    type="button"
                className="flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded">
                Lancer l'entraînement </button>
                </div>    
            </div>
            <div className="flex items-center my-8 pl-8">
                {ReponseTomatos && (
                    <div className="mr-4">
                        <p className={`text-lg font-medium ${ReponseTomatos.includes('succès') ? 'text-green-500' : 'text-red-500'}`}>
                            {ReponseTomatos}
                        </p>
                    </div>
                )}
               
            </div>
           
                </form>
            </div>

            <div className="mx-4 ">
                <form>
                <div className="flex items-center my-8 pl-4">
               <p className="text-xl font-medium mt-5 leading-none text-teal-500 ">
               L'entraînement du module GAN pour le fichier Maïs :</p>
            </div>
                
            <div className="flex py-2">
           
              <div className='flex'> 
                <div className="flex items-center my-4 pl-4">
                  <p className="text-lg font-medium mt-5 ml-4  mr-3 leading-none text-gray-500 ">
                  Indique le nombre d'itérations pour entraîner votre module :
                    </p>
                </div>
                <div className="w-1/2 m-2 items-center border-b border-teal-500 py-4 px-2">
                    <input
                        type="number"
                        placeholder="nombre d'itérations"
                        className="appearance-none bg-transparent border-none w-full text-gray-700 py-1 px-2 leading-tight focus:outline-none"
                        value={NbiterartionMais} // Utilisation de la variable d'état correspondante
                        onChange={(e) => setNbiterartionMais(parseInt(e.target.value))} // Assurez-vous de convertir la valeur en entier avec parseInt
                    />
                </div>
                </div> 
                <div className="w-1/5 m-5 items-center ">
                    <button
                    onClick={(e) => {
                        setReponseMais("Veuillez patienter jusqu'à la fin de l'entraînement du GAN.");
                        e.preventDefault();
                        handlelancerEntraianementMais(e);
                    }}
                    type="button"
                className="flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded">
                Lancer l'entraînement </button>
                </div>    
            </div>
            <div className="flex items-center my-8 pl-8">
                {ReponseMais && (
                    <div className="mr-4">
                        <p className={`text-lg font-medium ${ReponseMais.includes('succès') ? 'text-green-500' : 'text-red-500'}`}>
                            {ReponseMais}
                        </p>
                    </div>
                )}
               
            </div>
           
                </form>
            </div>

            <div className="mx-4 ">
                <form>
                <div className="flex items-center my-8 pl-4">
               <p className="text-xl font-medium mt-5 leading-none text-teal-500 ">
               L'entraînement du module GAN pour le fichier Blé :</p>
            </div>
                
            <div className="flex py-2">
           
              <div className='flex'> 
                <div className="flex items-center my-4 pl-4">
                  <p className="text-lg font-medium mt-5 ml-4  mr-3 leading-none text-gray-500 ">
                  Indique le nombre d'itérations pour entraîner votre module :
                    </p>
                </div>
                <div className="w-1/2 m-2 items-center border-b border-teal-500 py-4 px-2">
                    <input
                        type="number"
                        placeholder="nombre d'itérations"
                        className="appearance-none bg-transparent border-none w-full text-gray-700 py-1 px-2 leading-tight focus:outline-none"
                        value={NbiterartionBle} // Utilisation de la variable d'état correspondante
                        onChange={(e) => setNbiterartionBle(parseInt(e.target.value))} // Assurez-vous de convertir la valeur en entier avec parseInt
                    />
                </div>
                </div> 
                <div className="w-1/5 m-5 items-center ">
                    <button
                    onClick={(e) => {
                        setReponseBle("Veuillez patienter jusqu'à la fin de l'entraînement du GAN.");
                        e.preventDefault();
                        handlelancerEntraianementBle(e);
                    }}
                    type="button"
                className="flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded">
                Lancer l'entraînement </button>
                </div>    
            </div>
            <div className="flex items-center my-8 pl-8">
                {ReponseBle && (
                    <div className="mr-4">
                        <p className={`text-lg font-medium ${ReponseBle.includes('succès') ? 'text-green-500' : 'text-red-500'}`}>
                            {ReponseBle}
                        </p>
                    </div>
                )}
               
            </div>
           
                </form>
            </div>

            <div className="mx-4 ">
                <form>
                <div className="flex items-center my-8 pl-4">
               <p className="text-xl font-medium mt-5 leading-none text-teal-500 ">
               L'entraînement du module GAN pour le fichier Riz :</p>
            </div>
                
            <div className="flex py-2">
           
              <div className='flex'> 
                <div className="flex items-center my-4 pl-4">
                  <p className="text-lg font-medium mt-5 ml-4  mr-3 leading-none text-gray-500 ">
                  Indique le nombre d'itérations pour entraîner votre module :
                    </p>
                </div>
                <div className="w-1/2 m-2 items-center border-b border-teal-500 py-4 px-2">
                    <input
                        type="number"
                        placeholder="nombre d'itérations"
                        className="appearance-none bg-transparent border-none w-full text-gray-700 py-1 px-2 leading-tight focus:outline-none"
                        value={NbiterartionRiz} 
                        onChange={(e) => setNbiterartionRiz(parseInt(e.target.value))} // Assurez-vous de convertir la valeur en entier avec parseInt
                    />
                </div>
                </div> 
                <div className="w-1/5 m-5 items-center ">
                    <button
                    onClick={(e) => {
                        setReponseRiz("Veuillez patienter jusqu'à la fin de l'entraînement du GAN.");
                        e.preventDefault();
                        handlelancerEntraianementRiz(e);
                    }}
                    type="button"
                className="flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded">
                Lancer l'entraînement </button>
                </div>    
            </div>
           
                </form>
                <div className="flex items-center my-8 pl-8">
                {ReponseRiz && (
                    <div className="mr-4">
                        <p className={`text-lg font-medium ${ReponseRiz.includes('succès') ? 'text-green-500' : 'text-red-500'}`}>
                            {ReponseRiz}
                        </p>
                    </div>
                )}
               
            </div>
            </div>

            <div className="mx-4 ">
                <form>
                <div className="flex items-center my-8 pl-4">
               <p className="text-xl font-medium mt-5 leading-none text-teal-500 ">
               L'entraînement du module GAN pour le fichier Arachide et riz :</p>
            </div>
                
            <div className="flex py-2">
           
              <div className='flex'> 
                <div className="flex items-center my-4 pl-4">
                  <p className="text-lg font-medium mt-5 ml-4  mr-3 leading-none text-gray-500 ">
                  Indique le nombre d'itérations pour entraîner votre module :
                    </p>
                </div>
                <div className="w-1/2 m-2 items-center border-b border-teal-500 py-4 px-2">
                    <input
                        type="number"
                        placeholder="nombre d'itérations"
                        className="appearance-none bg-transparent border-none w-full text-gray-700 py-1 px-2 leading-tight focus:outline-none"
                        value={NbiterartionArachid_riz} 
                        onChange={(e) => setNbiterartionArachid_riz(parseInt(e.target.value))} // Assurez-vous de convertir la valeur en entier avec parseInt
                    />
                </div>
                </div> 
                <div className="w-1/5 m-5 items-center ">
                    <button
                    onClick={(e) => {
                        setReponseArachid_riz("Veuillez patienter jusqu'à la fin de l'entraînement du GAN.");
                        e.preventDefault();
                        handlelancerEntraianementArachid_riz(e);
                    }}
                    type="button"
                className="flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded">
                Lancer l'entraînement </button>
                </div>    
            </div>
           
                </form>
                <div className="flex items-center my-8 pl-8">
                {ReponseArachid_riz && (
                    <div className="mr-4">
                        <p className={`text-lg font-medium ${ReponseArachid_riz.includes('succès') ? 'text-green-500' : 'text-red-500'}`}>
                            {ReponseArachid_riz}
                        </p>
                    </div>
                )}
               
            </div>
            </div>

            <div className="mx-4 ">
                <form>
                <div className="flex items-center my-8 pl-4">
               <p className="text-xl font-medium mt-5 leading-none text-teal-500 ">
               L'entraînement du module GAN pour le fichier  Data plants:</p>
            </div>
                
            <div className="flex py-2">
           
              <div className='flex'> 
                <div className="flex items-center my-4 pl-4">
                  <p className="text-lg font-medium mt-5 ml-4  mr-3 leading-none text-gray-500 ">
                  Indique le nombre d'itérations pour entraîner votre module :
                    </p>
                </div>
                <div className="w-1/2 m-2 items-center border-b border-teal-500 py-4 px-2">
                    <input
                        type="number"
                        placeholder="nombre d'itérations"
                        className="appearance-none bg-transparent border-none w-full text-gray-700 py-1 px-2 leading-tight focus:outline-none"
                        value={NbiterartionDataPlants} 
                        onChange={(e) => setNbiterartionDataPlants(parseInt(e.target.value))} // Assurez-vous de convertir la valeur en entier avec parseInt
                    />
                </div>
                </div> 
                <div className="w-1/5 m-5 items-center ">
                    <button
                    onClick={(e) => {
                        setReponseDataPlants("Veuillez patienter jusqu'à la fin de l'entraînement du GAN.");
                        e.preventDefault();
                        handlelancerEntraianementDataPlants(e);
                    }}
                    type="button"
                className="flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded">
                Lancer l'entraînement </button>
                </div>    
            </div>
           
                </form>
            <div className="flex items-center my-8 pl-8">
                {ReponseDataPlants && (
                    <div className="mr-4">
                        <p className={`text-lg font-medium ${ReponseDataPlants.includes('succès') ? 'text-green-500' : 'text-red-500'}`}>
                            {ReponseDataPlants}
                        </p>
                    </div>
                )}
               
            </div>
            </div>

            <div className="mx-4 ">
                <form>
                <div className="flex items-center my-8 pl-4">
               <p className="text-xl font-medium mt-5 leading-none text-teal-500 ">
               L'entraînement du module GAN pour le fichier Web site plants:</p>
            </div>
            <div className="flex py-2">
           
              <div className='flex'> 
                <div className="flex items-center my-4 pl-4">
                  <p className="text-lg font-medium mt-5 ml-4  mr-3 leading-none text-gray-500 ">
                  Indique le nombre d'itérations pour entraîner votre module :
                    </p>
                </div>
                
            <div className="w-1/2 m-2 items-center border-b border-teal-500 py-4 px-2">
                <input
                    type="number"
                    placeholder="nombre d'itérations"
                    className="appearance-none bg-transparent border-none w-full text-gray-700 py-1 px-2 leading-tight focus:outline-none"
                    value={NbiterartionWebsitePlants}
                    onChange={(e) => setNbiterartionWebsitePlants(parseInt(e.target.value))} // Assurez-vous de convertir la valeur en entier avec parseInt
                />
            </div>
            </div>
                <div className="w-1/5 m-5 items-center ">
                        <button
                        onClick={(e) => {e.preventDefault();
                            setReponseWebsitePlants("Veuillez patienter jusqu'à la fin de l'entraînement du GAN.");
                            handlelancerEntraianementWebsitePlants(e);
                        }}
                        type="button"
                    className="flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded">
                    Lancer l'entraînement </button>
                    </div> 
                </div>
           
                </form>
            <div className="flex items-center my-8 pl-8">
                {ReponseWebsitePlants && (
                    <div className="mr-4">
                        <p className={`text-lg font-medium ${ReponseWebsitePlants.includes('succès') ? 'text-green-500' : 'text-red-500'}`}>
                            {ReponseWebsitePlants}
                        </p>
                    </div>
                )}
               
            </div>
            </div>




              
    </div> 
    
      );
    }


export default Entrainement;
