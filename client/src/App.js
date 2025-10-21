import React, { useEffect, useState } from 'react';

function App() {
  const [pets, setPets] = useState([]);

  useEffect(() => {
    fetch('/api/pets')
      .then(res => res.json())
      .then(data => setPets(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="App">
      <h1>سوپر اپلیکیشن حیوانات خانگی</h1>
      {pets.map(pet => (
        <div key={pet.id} className="pet-card">
          <h3>{pet.name}</h3>
          <p>{pet.type}</p>
        </div>
      ))}
    </div>
  );
}

export default App;
