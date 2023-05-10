import React, { useState } from 'react';

const pageStyles = {
  color: '#232129',
  padding: 96,
  fontFamily: '-apple-system, Roboto, sans-serif, serif',
};

const IndexPage = () => {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('No Name');

  return (
    <main style={pageStyles}>
      <h1>Counter</h1>
      <h3>カウント: {count}</h3>
      <button onClick={() => setCount(count + 1)}>+</button>
      <button onClick={() => setCount(count - 1)}>-</button>

      <h1>Name</h1>
      <h3>{name}さん、こんにちは</h3>
      <input onChange={(e) => setName(e.target.value)}></input>
    </main>
  );
};

export default IndexPage;

export const Head = () => <title>Home Page</title>;
