var nodes = JSON.parse('{{ nodes|escapejs }}');
var edges = JSON.parse('{{ edges|escapejs }}');
var i=0;
nodes.forEach(function(data) {
    nodes[i]["shape"] = 'image';
    switch(nodes[i]["type"]){
        case 'network':
            $images = "{% static 'icons/switch.png' %}";
            break;
        case 'server':
            $images = "{% static 'icons/controller_server.png' %}";
            break;
        case 'firewall':
            $images = "{% static 'icons/firewall.png' %}";
            break;
        default:
            $images = "{% static 'icons/group_user.png' %}";
            break;
    }
    nodes[i]['image'] = $images;
    i+=1;
});
console.log(nodes);
// var options = {
//       interaction: {
//          zoomView: true, // nonaktifkan zoom
//          dragNodes: true // aktifkan geser node
//       },
//       physics: {
//          enabled: true,
//          stabilization: true // aktifkan animasi stabilitasi
//       },
//       layout: {
//          hierarchical: {
//             direction: 'UD', // arah tata letak kiri ke kanan
//             // sortMethod: 'directed' // urutkan berdasarkan arah edge
//          }
//       },
//       interaction: {
//          hover: true
//       }
//    };
var options = 
{
    layout:{
            randomSeed:2
    },
    "nodes": {
        shape : 'circle',
    },
    "edges": {
        arrows: {
            to:     {enabled: true, scaleFactor:0.5},
        },
        "smooth": {
            enabled: false
        },
        font: {
            size: 14,
            color: "red",
            face: "sans",
            background: "white",
            strokeWidth:3,
            align: "middle",
            strokeWidth: 2
        }
    },
    "physics": {
        "barnesHut": {
            "gravitationalConstant": -2000,
            "centralGravity": 0.3,
            "springLength": 200,
            "springConstant": 0.04,
            "damping": 0.09,
            "avoidOverlap": 1
        },

        "forceAtlas2Based": {
            "gravitationalConstant": -50,
            "centralGravity": 0.01,
            "springLength": 200,
            "springConstant": 0.08,
            "damping": 0.4,
            "avoidOverlap": 1
        },

        "repulsion": {
            "centralGravity": 0.2,
            "springLength": 250,
            "springConstant": 0.2,
            "nodeDistance": 200,
            "damping": 0.07
        },

        "hierarchicalRepulsion": {
            "nodeDistance": 300,
            "centralGravity": 0.2,
            "springLength": 300,
            "springConstant": 0.2,
            "damping": 0.07
        },

    "maxVelocity": 50,
    "minVelocity": 0.4,
    "solver": "hierarchicalRepulsion",
    "stabilization": {
        "enabled": true,
        "iterations": 1000,
        "updateInterval": 100,
        "onlyDynamicEdges": false,
        "fit": true
    },

    "timestep": 0.4,
    }
};

var container = document.getElementById('topologyDiv');
var data = {
    nodes: nodes,
    edges: edges,
    stabilize: true
};  

var network = new vis.Network(container, data, options);
network.on('click', function (properties) {
    if (properties.nodes > 0) {
            window.location.href = "health/processor/"+properties.nodes
    }
});
