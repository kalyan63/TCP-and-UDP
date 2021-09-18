## This is the Answers for the 1st Question

1. **Time Difference in ms:** 

    > 
        |       File Name           |   Tcp         |   Udp         | 
        _____________________________________________________________

        | DreamDays.txt             |   58.8        |   24.75       |

        | FamilyOfEngineers.txt     |   57.11       |   29.44       |

        | IntroToRobertBrowning.txt |   44.11       |   40.44       |

        | LifeAndDeath.txt          |   14.56       |   12.12       |

        | WarAndPeace.txt           |   212.9       |   174.6       |

2. **Throughput achieved by TCP and UDP is:**

    > Throughput = Number of bits transferred per unit time. 

    > Here throughput can be calculated by using average throughput acheived by transfering all the files.

    > Throughput in MB/s

        |       File Name           |   Size in KB  |   Tcp Throughput  |   Udp Throughput  | 
        _____________________________________________________________________________________

        | DreamDays.txt             |   234         |   4.03            |   9.45            |

        | FamilyOfEngineers.txt     |   234         |   4.09            |   7.95            |

        | IntroToRobertBrowning.txt |   699         |   15.84           |   17.29           |

        | LifeAndDeath.txt          |   123         |   8.44            |   10.14           |

        | WarAndPeace.txt           |   3281        |   15.41           |   18.8            |

    > Tcp throughput = 9.56  MB/s

    > Udp throughput = 12.72 MB/s

3. **Word Count and Line Count:**

    > 
        |       File Name           |     Tcp       |       Udp     | 
        _____________________________________________________________

        | DreamDays.txt             | 4175, 41075   | 4175, 41075   |

        | FamilyOfEngineers.txt     | 4175, 41075   | 4175, 41075   |

        | IntroToRobertBrowning.txt | 16176, 113366 | 16176, 113366 |

        | LifeAndDeath.txt          | 2910, 21178   | 2910, 21178   |

        | WarAndPeace.txt           | 66029, 566334 | 66029, 566334 |

    > There was no Difference in file when done using diff and wc        

4. **Test on Test.txt file of size 10KB:** 

    > 
        |       File Name           |     Tcp       |       Udp     | 
        _____________________________________________________________

        | Word Count and line count | 867, 1274     | 867, 1274     |  

        |   Time in ms              |   14.011      |   8.36        |
    
    > There was no Difference in file when done using diff and wc