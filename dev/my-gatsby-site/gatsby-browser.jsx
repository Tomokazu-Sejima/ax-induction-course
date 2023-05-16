import React from 'react';
import MyLayout from './src/components/Layout';

// Wraps every page in a component
export const wrapPageElement = ({ element, props }) => {
  return <MyLayout {...props}>{element}</MyLayout>;
};
