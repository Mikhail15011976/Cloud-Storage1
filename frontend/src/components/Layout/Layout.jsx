import React from 'react';
import './Layout.css';

const Layout = ({ children }) => {
  return (
    <div className="layout">
      <header className="layout-header">
        <h1>Cloud Storage</h1>
      </header>
      <main className="layout-content">
        {children}
      </main>
      <footer className="layout-footer">
        © {new Date().getFullYear()} Cloud Storage
      </footer>
    </div>
  );
};

export default Layout;