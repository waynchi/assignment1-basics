from tests.adapters import run_train_bpe

run_train_bpe(
    "/home/waynechi/dev/cs336/assignment1-basics/data/TinyStoriesV2-GPT4-train.txt",
    10000,
    ["<|endoftext|>"],
)
