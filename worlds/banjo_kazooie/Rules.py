from worlds.generic.Rules import add_rule, set_rule, forbid_item

def can_long_jump(state, player): 
        return (
            state.has("Double Jump", player)
            or state.has("Rat-At-Tat Rap", player)
            or state.has("Talon Trot", player)
        )

def set_rules(self) -> None:
    # Spiral Mountain
    set_rule(self.world.get_location("SM HC Stump", self.player), lambda state: 
        state.has("FlapFlip", self.player) 
        or state.has("Talon Trot", self.player)
        or (self.hard_mode 
            and state.has("High Jump", self.player)
            and state.has("Rat-At-Tat Rap", self.player)
        )
    )
    set_rule(self.world.get_location("SM HC Tree", self.player), lambda state: 
        state.has("FlapFlip", self.player) 
        or (
            state.has("Climbing", self.player)
            and (
                state.has("High Jump", self.player)
                or state.has("Talon Trot", self.player) # Remove if talon trot height can be reduced
            )
        )
    )
    set_rule(self.world.get_location("SM HC Waterfall", self.player), lambda state: 
        state.has("Talon Trot", self.player) 
        or (
            state.has("High Jump", self.player)
            and (
                state.has("Double Jump", self.player)
                or state.has("Rat-At-Tat Rap", self.player)
            )
        )
    )
    set_rule(self.world.get_location("SM HC Underwater", self.player), lambda state: 
        state.has("Diving", self.player) 
    )
    set_rule(self.world.get_location("SM HC Boulder", self.player), lambda state: 
        state.has("Beak Barge", self.player) 
        or state.has("Beak Buster", self.player)
    )
    set_rule(self.world.get_location("SM HC Coli", self.player), lambda state: 
        state.has("Rat-At-Tat Rap", self.player)
    )

    #Mumbo's Mountain
    set_rule(self.world.get_location("MM Jinjo Purple Pillar Starting Area", self.player), lambda state: 
        state.has("FlapFlip", self.player)
        or can_long_jump(state, self.player)
    )
    set_rule(self.world.get_location("MM Jinjo Blue Lake", self.player), lambda state: 
        state.has("High Jump", self.player)
        or can_long_jump(state, self.player)
    )
    set_rule(self.world.get_location("MM Jinjo Green Inside Hut", self.player), lambda state: 
        state.has("Beak Buster", self.player)
    )

    set_rule(self.world.get_location("MM Jiggy Middle of Stonehenge", self.player), lambda state: 
        self.hard_mode 
        or state.has("High Jump", self.player)
        or state.has("FlapFlip", self.player)
        or can_long_jump(state, self.player)
    )
    set_rule(self.world.get_location("MM Jiggy Give Monkey Orange", self.player), lambda state: 
        state.has("Climbing", self.player)
        or state.has("FlapFlip", self.player)
        or (
            self.hard_mode
            and (
                state.has("High Jump", self.player)
                or state.has("Beak Buster", self.player)
            )
        )
    )
    set_rule(self.world.get_location("MM Jiggy Beat Conga", self.player), lambda state: 
        state.has("FlapFlip", self.player)
        and state.has("Eggs", self.player)
    )
    set_rule(self.world.get_location("MM Jiggy Inside Hut", self.player), lambda state: 
        state.has("Beak Buster", self.player)
    )
    set_rule(self.world.get_location("MM Jiggy Feed Spinning Totem", self.player), lambda state: 
        state.has("Eggs", self.player)
    )
    set_rule(self.world.get_location("MM Jiggy Mumbo's Hut Eye", self.player), lambda state: 
        state.has("FlapFlip", self.player)
    )

    set_rule(self.world.get_location("MM Token Ticker's Tower", self.player), lambda state: 
        #Needs access rule if entering from the top
        state.has("Talon Trot", self.player) 
        or state.has("FlapFlip", self.player)
        or state.has("High Jump", self.player)
        or state.has("Mumbo Tokens", self.player, 5) 
        or (
            self.hard_mode
            and (
                state.has("Double Jump", self.player)
                or state.has("Rat-At-Tat Rap", self.player)
            )
        )
    )

    set_rule(self.world.get_location("MM HC Top of Spinning Totem", self.player), lambda state: 
        state.has("Eggs", self.player)
        and (
            state.has("Talon Trot", self.player) 
            or state.has("FlapFlip", self.player)
            or (
                #Hard mode?
                state.has("High Jump", self.player)
                and state.has("Beak Buster", self.player)
                and (
                    state.has("Double Jump", self.player)
                    or state.has("Rat-At-Tat Rap", self.player)
                )
            )    
        )
    )
    set_rule(self.world.get_location("MM HC Lake Cave", self.player), lambda state: 
        self.hard_mode
        or (
            not self.hard_mode
            and state.has("Mumbo Tokens", self.player, 5)
        )
    )

    # Grunty's Lair
    set_rule(self.world.get_location("GL Jiggy Mumbo's Mountain Switch", self.player), lambda state: 
       state.has("Mumbo Tokens", self.player, 5) 
       #can access mumbos hut, and has spent the 5 tokens to unlock
    )