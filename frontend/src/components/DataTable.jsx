
import React from 'react';

function DataTable() {
  return (
    <div className="data-table">
      <h3>DataTable</h3>
      <table>
        <thead>
          <tr>
            <th>Kreftform</th><th>Region</th><th>Kjønn</th><th>Tilfeller</th><th>Rate_ujustert</th><th>ASR_Norge</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>Bryst</td><td>Helse Sør-Øst</td><td>Kvinner</td><td>2408</td><td>152.2</td><td>138.7</td></tr>
        </tbody>
      </table>
    </div>
  );
}

export default DataTable;
