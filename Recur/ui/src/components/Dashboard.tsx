
import React from 'react';

const ghostTeams = [
  {
    name: 'Team Alpha',
    color: '#FF6F61',
    emoji: '👻',
    description: 'Coding & Automation',
    members: [
      'Zephyr', 'Bolt', 'Synapse', 'Nexus', 'Echo', 'Prism', 'Sentinel', 'Luna'
    ]
  },
  {
    name: 'Team Beta',
    color: '#5F4B8B',
    emoji: '👻',
    description: 'Research & Brainstorming',
    members: [
      'Sage', 'Pulse', 'Harmony', 'Atlas', 'Muse', 'Flux', 'Unity', 'Chroma'
    ]
  }
];

const Dashboard: React.FC = () => {
  return (
    <div style={{
      background: 'linear-gradient(135deg, #f5f5f5 0%, #e0e0e0 100%)',
      minHeight: '100vh',
      fontFamily: '"Adobe Clean", "Segoe UI", Arial, sans-serif',
      color: '#222',
      padding: '2rem',
      boxShadow: '0 0 40px 0 rgba(0,0,0,0.08)'
    }}>
      <h1 style={{
        fontWeight: 700,
        fontSize: '2.5rem',
        letterSpacing: '0.02em',
        marginBottom: '1.5rem',
        color: '#333',
        textShadow: '0 2px 8px #fff'
      }}>
        👻 Recur Dashboard
      </h1>
      <div style={{
        display: 'flex',
        gap: '2rem',
        flexWrap: 'wrap',
        justifyContent: 'center'
      }}>
        {ghostTeams.map(team => (
          <div key={team.name} style={{
            background: '#fff',
            borderRadius: '1.5rem',
            boxShadow: `0 4px 24px 0 ${team.color}33`,
            padding: '2rem',
            minWidth: '320px',
            maxWidth: '340px',
            margin: '1rem 0',
            textAlign: 'center',
            border: `2px solid ${team.color}`
          }}>
            <div style={{ fontSize: '2.5rem', marginBottom: '0.5rem' }}>{team.emoji}</div>
            <h2 style={{
              color: team.color,
              fontWeight: 600,
              fontSize: '1.5rem',
              marginBottom: '0.5rem'
            }}>{team.name}</h2>
            <div style={{ fontSize: '1rem', marginBottom: '1rem', color: '#666' }}>{team.description}</div>
            <div style={{
              display: 'flex',
              flexWrap: 'wrap',
              gap: '0.5rem',
              justifyContent: 'center'
            }}>
              {team.members.map(member => (
                <span key={member} style={{
                  background: team.color,
                  color: '#fff',
                  borderRadius: '1rem',
                  padding: '0.5rem 1rem',
                  fontWeight: 500,
                  fontSize: '1rem',
                  boxShadow: '0 2px 8px 0 #0001',
                  letterSpacing: '0.01em'
                }}>
                  {team.emoji} {member}
                </span>
              ))}
            </div>
          </div>
        ))}
      </div>
      <div style={{
        marginTop: '3rem',
        fontSize: '1.1rem',
        color: '#888',
        textAlign: 'center'
      }}>
        <span role="img" aria-label="sparkles">✨</span> Polished Adobe-inspired UI/UX powered by MoE Ghost Teams <span role="img" aria-label="sparkles">✨</span>
      </div>
    </div>
  );
};

export default Dashboard;
