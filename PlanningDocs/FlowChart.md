
``` mermaid

flowchart TD
    subgraph a[Character Creation]
        A[Start Menu] --> B{Gender?}
        B -- Male/Female --> C{Orientation?}
        C --> O1[Gay] 
        C --> O2[Straight] 
        C --> O3[Bi]
    end
    O1 --> H[Home]
    O2 --> H
    O3 --> H

    subgraph b[Gay Story]
    
    end

    subgraph c[Straight Story]
    
    end

    subgraph d[Bi Story]

    end

   

```