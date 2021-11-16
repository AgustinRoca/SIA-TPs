import json


class Config:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            cfg = json.load(f)

        self.input = cfg['input']

        self.system_threshold = cfg['training']['system_threshold']
        self.training_ratio = cfg['training']['training_ratio']
        self.data_random_seed = cfg['training']['data_random_seed']
        self.normalize = cfg['training']['normalize']
        self.eta = cfg['training']['eta']
        self.error_threshold = cfg['training']['error_threshold']
        self.epochs = cfg['training']['epochs']
        self.trust = cfg['training']['trust']
        self.use_trust = cfg['training']['use_trust']

        self.system = cfg['network']['system']
        self.beta = cfg['network']['beta']
        self.mid_layout = cfg['network']['mid_layout']
        self.latent_dim = cfg['network']['latent_dim']
        self.randomize_w = cfg['network']['randomize_w']
        self.randomize_w_ref = cfg['network']['randomize_w_ref']
        self.randomize_w_by_len = cfg['network']['randomize_w_by_len']

        self.momentum = cfg['momentum']['momentum']
        self.alpha = cfg['momentum']['alpha']

        self.optimizer = cfg['optimizer']['optimizer']
        self.iter = cfg['optimizer']['iter']
        self.fev = cfg['optimizer']['fev']

        self.den_pm = cfg['den_pm']
        self.plot = cfg['plot']
