"""
LEGB Scope Rule Masterclass
This script demonstrates how Python searches for variable names 
using a practical customer service queue scenario.
"""

# ==========================================
# 4. BUILT-IN SCOPE (B)
# ==========================================
# Python has pre-defined names like `max`, `len`, `print`, and `ValueError`.
# We don't need to define them; they are always available.
# Example: We will use the built-in max() function later.


# ==========================================
# 3. GLOBAL SCOPE (G)
# ==========================================
# Variables defined at the top level of the file.
# They can be read from anywhere inside this module.
platform_name = "BetWin Casino"
total_active_users = 1500

def manage_customer_queue():
    # ==========================================
    # 2. ENCLOSING SCOPE (E)
    # ==========================================
    # Variables defined in an outer function.
    # Accessible to the outer function AND any nested (inner) functions.
    queue_status = "High Volume"
    agent_capacity = 5
    
    def process_user_chat(username):
        # ==========================================
        # 1. LOCAL SCOPE (L)
        # ==========================================
        # Variables defined inside this specific, innermost function.
        # They CANNOT be accessed outside of 'process_user_chat'.
        chat_duration_minutes = 12
        
        print(f"--- Processing Chat for {username} ---")
        
        # SEARCH ORDER DEMONSTRATION:
        
        # Python checks LOCAL first. It finds 'chat_duration_minutes' right here.
        print(f"Duration: {chat_duration_minutes} mins.")
        
        # Python checks LOCAL -> not found. Checks ENCLOSING -> found 'queue_status'!
        print(f"Current Queue Status: {queue_status}")
        
        # Python checks LOCAL -> ENCLOSING -> not found. Checks GLOBAL -> found 'platform_name'!
        print(f"Platform: {platform_name}")
        
        # Python checks LOCAL -> ENCLOSING -> GLOBAL -> not found. Checks BUILT-IN -> found 'max()'!
        # It uses the built-in max() function to ensure the score doesn't drop below 1.
        efficiency_score = max(1, agent_capacity - (chat_duration_minutes / 10))
        print(f"Agent Efficiency Score: {efficiency_score:.2f}\n")

    # We call the inner function from the outer function
    process_user_chat("Player777")
    
    # ❌ UNCOMMENTING THE LINE BELOW WILL CAUSE AN ERROR
    # print(chat_duration_minutes) 
    # Why? Because 'chat_duration_minutes' is LOCAL to process_user_chat. 
    # The outer function cannot look "inward" to grab local variables.

if __name__ == "__main__":
    print("Starting system...\n")
    manage_customer_queue()
    
    # ❌ UNCOMMENTING THE LINE BELOW WILL CAUSE AN ERROR
    # print(queue_status)
    # Why? Because 'queue_status' is ENCLOSED inside manage_customer_queue.
    # It does not exist in the Global scope.




"""
Modifying Outer Scopes
1. The global Keyword (Modifying Global Scope)
Example: Tracking VIP escalations across a shift.
Using 'global' (Use with caution!)
"""

escalation_count = 0  # Global variable

def handle_vip_issue():
    # Without this line, Python would think we are trying to create
    # a NEW local variable called 'escalation_count'.
    global escalation_count 
    
    # Now we are modifying the global variable
    escalation_count += 1
    print(f"Issue resolved. Total escalations today: {escalation_count}")

handle_vip_issue()
handle_vip_issue()



"""
2. The nonlocal Keyword (Modifying Enclosing Scope)
Example: A session timer for a specific agent.
Using 'nonlocal'
"""

def agent_login_session(agent_name):
    active_chats = 0  # Enclosing variable
    
    def assign_new_chat():
        nonlocal active_chats # Tells Python to use the variable from agent_login_session
        active_chats += 1
        print(f"{agent_name} now has {active_chats} active chats.")
        
    return assign_new_chat

# Create a session for an agent
session = agent_login_session("Alex")
session() # Alex now has 1 active chats.
session() # Alex now has 2 active chats.

"""
🌟 The "Best Practice" Alternative
pass data in as arguments and pass data out using return
The Clean Way: No globals, no nonlocals. Just inputs and outputs.
"""
def add_new_chat(current_chat_count):
    """Takes the current count, returns the updated count."""
    return current_chat_count + 1

# The state is managed outside, and passed into the function when needed.
alex_chats = 0
alex_chats = add_new_chat(alex_chats)
alex_chats = add_new_chat(alex_chats)
print(f"Alex's final chat count: {alex_chats}")
