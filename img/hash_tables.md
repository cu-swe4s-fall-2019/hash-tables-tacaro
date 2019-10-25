# Hash Tables and Functions

Put simply: A hash function takes a key as an argument and returns the index at which the corresponding value exists. `h(key) = index` A hash function and an array make a "hash table". As an example, let's consider the following parallel arrays.

```
samples = [S1, S2, S3, S4, S5]
tissues = [Blood, Brain, Heart, Muscle, Skin]
```

h(), our hash function, must be a perfect hash: no two keys can ever hash to the same index! The issue is that this takes up a lot of space. For example, what if we only had two values: `h(S1) = 0` and `h(S1000) = 999`. We'd still need 1000 elements in our array!

One solution is to pre-specify the size of our value array so as not to be unrealistically large. For the two values above, let's be safe and say our array can have 5 elements, two for our elements and three empty. Because our array has _five_ elements, we can use modulo five _%5_ in our hash function to assign array indexes. I'll call this new slick hash function "k"

key   | value | h(key) | k(key)
----- | ----- | ------ | ------
S1    | Blood | 0      | 0
S1000 | Nerve | 999    | 4

tissues = [Blood,,,,Nerve]

Though, as you can probably guess, if we're using the modulo, it isn't out of the question that more than one number modulo to the same value. For example 999%5 = 4, 74%5 = 4\. Thus, the likelihood that two keys hash to the same index is (1/N) where N is the size of the array (like rolling dice). It follows that the likelihood of a collision in a given array is (M/N) where M is the number of keys inserted (like rolling a dice multiple times). We call this number the "load factor".

Sure, we can increase N, the size of the array, but that doesn't solve the problem. After inserting M keys, the expected value of collisions is (M choose 2)(1/N) = (M(M-1))/(2N) Sadly, as we can see, collisions grows quadratically with the size of the array growing linearly.

Typically, hash tables will limit collisions by doubling their size (N = 2N) when the load factor passes some threshold that the programmer determines. This process is called rehashing, and it requires that all keys in the array must be rehashed to the new array size.

## Linear Probing

is a solution to collisions. To create our hash table... _Insertion_

1. Run the hash function, open the table at the hash slot given by the hash function.
2. If the hash slot is taken, scan the array until the first open slot is found.
3. Insert at open slot.

_Searching_

1. Start at the hashed index that was given by the hash function
2. Scan the array until the index with a matching key is found.
3. Retrieve.

Let's follow this example:

key   | value  | h(key)%5 | hash table
----- | ------ | -------- | -------------------------------------------
S1    | Blood  | 0        | [(S1,Blood),,,,]
S1000 | Nerve  | 4        | [(S1,Blood),,,,(S1000,Nerve)]
S215  | Kidney | 4        | [(S1,Blood), (S215,Kidney),,,(S1000,Nerve)]

When inserting S215 at index 4, we get a hash collision! So, no sweat, we just insert it at index...wait..4 was the last index. No sweat! We'll just put it at index zero..ah..but S1,Blood is there...no sweat! Put it at index 1\. All good. Totally fine.

When searching for S215 we start at its hash value, 4\. There we find S1000,Nerve. Not right...let's loop around to the beginning of the array...S1,Blood...still not right...ah! It's at index 1\. Retrieve it.

## Chained Hash

Another way to deal with collisions is to use lists of lists. Each element in the hash table is a list containing key, value pairs. If two values hash to the same index, you just append that key, value pair to the list. When searching, you scan the list at the hashed index for a matching key.
