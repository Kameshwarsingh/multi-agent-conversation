
from autogen import ConversableAgent
from autogen import GroupChat
from autogen import GroupChatManager


llm_config={"config_list": [{"model": "TheBloke/OpenHermes-2.5-Mistral-7B-GGUF", "base_url":"http://localhost:1234/v1" , "api_key":"lm-studio" }]}

# Developer-role
developer_agent = ConversableAgent(
    name="developer_agent",
    system_message="You are helpful AI and help users with python code.\nYou will collaborate in multi-agent conversation and write python code.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

# Lead developer role
lead_developer_agent = ConversableAgent(
    name="lead_developer_agent",
    system_message="You are helpful AI and help in python code review.\nYou provide feedback and review comments to improve python code quality, ensure test cases are written.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)



group_chat = GroupChat(
    agents=[developer_agent, lead_developer_agent, ],
    messages=[],
    max_round=6,
    speaker_selection_method='round_robin',
    allow_repeat_speaker=False,
   

)

group_chat_manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config,
)

chat_result = lead_developer_agent.initiate_chat(
    group_chat_manager,
    message="Write a python function code to add two integer numbers.\nAlso write unit test case for the function.",
    summary_method="reflection_with_llm",
     temperature=0.3,
)


print(chat_result.summary)
