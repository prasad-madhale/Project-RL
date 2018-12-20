from gym.envs.registration import register

register(
    id='gamblers-v0',
    entry_point='gym_gamblers.envs:GamblersEnv',
)