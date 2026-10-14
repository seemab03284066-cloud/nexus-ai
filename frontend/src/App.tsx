import React, { useState, useEffect } from 'react';
import { 
  LayoutDashboard, Activity, Cpu, Layers, FileText, 
  History, ShieldAlert, Sliders, Bell, Settings as SettingsIcon, Wallet 
} from 'lucide-react';

export default function App() {
  const [activeTab, setActiveTab] = useState('overview');
  const [status, setStatus] = useState<any>(null);

  useEffect(() => {
    fetch('http://localhost:8000/')
      .then(res => res.json())
      .then(data => setStatus(data))
      .catch(err => console.error("Backend offline:", err));
  }, []);

  const tabs = [
    { id: 'overview', label: 'Overview', icon: LayoutDashboard },
    { id: 'market', label: 'Live Market', icon: Activity },
    { id: 'ai', label: 'AI Analysis', icon: Cpu },
    { id: 'trades', label: 'Trades', icon: Layers },
    { id: 'orders', label: 'Orders', icon: FileText },
    { id: 'history', label: 'Trade History', icon: History },
    { id: 'risk', label: 'Risk Center', icon: ShieldAlert },
    { id: 'strategies', label: 'Strategies', icon: Sliders },
    { id: 'notifications', label: 'Notifications', icon: Bell },
    { id: 'settings', label: 'Settings', icon: SettingsIcon },
  ];

  return (
    <div className="min-h-screen flex flex-col md:flex-row bg-[#090d16] text-gray-100">
      {/* Sidebar / Navigation */}
      <aside className="w-full md:w-64 bg-[#0d1322] border-r border-gray-800 flex flex-col justify-between p-4">
        <div>
          <div className="flex items-center space-x-2 mb-8 px-2">
            <Wallet className="w-8 h-8 text-blue-500" />
            <div>
              <h1 className="font-bold text-lg tracking-wider text-white">NEXUS AI</h1>
              <span className="text-xs px-2 py-0.5 bg-blue-900/50 text-blue-300 rounded border border-blue-700">PAPER TRADING ONLY</span>
            </div>
          </div>

          <nav className="space-y-1 overflow-x-auto md:overflow-visible flex md:flex-col space-x-2 md:space-x-0 pb-2 md:pb-0">
            {tabs.map((tab) => {
              const Icon = tab.icon;
              const isActive = activeTab === tab.id;
              return (
                <button
                  key={tab.id}
                  onClick={() => setActiveTab(tab.id)}
                  className={`flex items-center space-x-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-colors whitespace-nowrap ${
                    isActive 
                      ? 'bg-blue-600 text-white shadow-lg shadow-blue-600/30' 
                      : 'text-gray-400 hover:bg-gray-800/50 hover:text-gray-200'
                  }`}
                >
                  <Icon className="w-5 h-5" />
                  <span>{tab.label}</span>
                </button>
              );
            })}
          </nav>
        </div>

        <div className="hidden md:block pt-4 border-t border-gray-800 text-xs text-gray-500">
          <p>Status: <span className={status ? "text-green-400 font-semibold" : "text-yellow-400 font-semibold"}>{status ? "Connected" : "Connecting..."}</span></p>
          <p className="mt-1">Starting Capital: $100.00</p>
        </div>
      </aside>

      {/* Main Content Area */}
      <main className="flex-1 p-4 md:p-8 overflow-y-auto">
        <header className="flex justify-between items-center mb-6 pb-4 border-b border-gray-800">
          <h2 className="text-xl md:text-2xl font-bold uppercase tracking-wide text-gray-100">
            {activeTab}
          </h2>
          <div className="flex items-center space-x-4">
            <div className="bg-gray-900 border border-gray-800 px-3 py-1.5 rounded-lg text-xs">
              <span className="text-gray-400">Virtual Balance:</span> <span className="text-green-400 font-bold">$100.00</span>
            </div>
          </div>
        </header>

        <div className="bg-[#0d1322] border border-gray-800 rounded-xl p-6 shadow-xl min-h-[400px]">
          {activeTab === 'overview' && (
            <div>
              <h3 className="text-lg font-semibold mb-4 text-blue-400">Portfolio Overview</h3>
              <p className="text-gray-400">Welcome to NEXUS AI Paper Trading Platform. Your virtual account is active with $100.00 starting capital.</p>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-6">
                <div className="bg-gray-900/50 p-4 rounded-lg border border-gray-800">
                  <span className="text-xs text-gray-400">Total Equity</span>
                  <p className="text-2xl font-bold text-white mt-1">$100.00</p>
                </div>
                <div className="bg-gray-900/50 p-4 rounded-lg border border-gray-800">
                  <span className="text-xs text-gray-400">Realized PnL</span>
                  <p className="text-2xl font-bold text-green-400 mt-1">$0.00</p>
                </div>
                <div className="bg-gray-900/50 p-4 rounded-lg border border-gray-800">
                  <span className="text-xs text-gray-400">Open Positions</span>
                  <p className="text-2xl font-bold text-blue-400 mt-1">0 / 5</p>
                </div>
              </div>
            </div>
          )}

          {activeTab !== 'overview' && (
            <div className="flex flex-col items-center justify-center h-64 text-center">
              <p className="text-gray-400 text-lg">Module <span className="text-blue-400 font-semibold">{activeTab}</span> is ready for deployment and active market data integration.</p>
            </div>
          )}
        </div>
      </main>
    </div>
  );
    }
    
