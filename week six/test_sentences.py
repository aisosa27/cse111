from sentence import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import pytest
def test_get_determiner():
        # Test the singular determiners.
        singular_determiners = ["the", "one","a"]
        # This loop will repeat the statements inside it 4 times.
        for _ in range(4):
            word = get_determiner(1)
            # Verify that the word returned from get_determiner is
            # one of the words in the singular_determiners list.
            assert word in singular_determiners
        # If a loop's counting variable is not used inside the
        # body of the loop, many programmers will use underscore
        # (_) as the variable name for the counting variable.
        # Test the plural determiners.
        plural_determiners = ["some", "many"]
        for _ in range(4):
            word = get_determiner(2)
            # Verify that the word returned from get_determiner
            # is one of the words in the plural_determiners list.
            assert word in plural_determiners
def test_get_noun():
        singular_nouns = ["adult", "bird", "boy", "car", "cat",
            "child", "dog", "girl", "man", "woman"]
        for _ in range(9):
            noun = get_noun(1)
            assert noun in singular_nouns
        plural_nouns = ["adults", "birds", "boys", "cars", "cats",
            "children", "dogs", "girls", "men", "women"]
        for _ in range(9):
            noun = get_noun(2)
            assert noun in plural_nouns
def test_get_verb():
        past_tense = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
        for _ in range(9):
            verb = get_verb(1 or 2,"past")
            assert verb in past_tense
        present_singular_tense = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
        for _ in range(9):
            verb = get_verb(1, "present")
            assert verb in present_singular_tense
        present_plural_tense = ["drink", "eat", "grow", "laugh", "think",
            "run", "sleep", "talk", "walk", "write"]
        for _ in range(9):
            verb = get_verb(2, "present")
            assert verb in present_plural_tense
        future_tense = ["will drink", "will eat", "will grow", "will laugh",
            "will think", "will run", "will sleep", "will talk",
            "will walk", "will write"]
        for _ in range(9):
            verb = get_verb(1 or 2, "future")
            assert verb in future_tense
def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    for _ in range(30):
        preposition = get_preposition()
        assert preposition in prepositions
def test_get_prepositional_phrase():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    determiners = ["the", "one","a", "some", "many"]
    nouns = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman","adults", "birds", "boys", "cars",
"cats",
        "children", "dogs", "girls", "men", "women"]
    prepositional_phrase = get_prepositional_phrase( "present")
    assert prepositional_phrase[3] in prepositions
    assert prepositional_phrase[4] in determiners
    assert prepositional_phrase[5] in nouns
pytest.main(["-v", "--tb=line", "-rN", "week six/test_sentences.py"])