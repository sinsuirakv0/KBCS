# v15.7.4 → v16.0.0 · 要調査の変更候補 (6)

[一覧の目次](README.md)

### [`00492380`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492380.md) → [`004b5218`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5218.md) _ZN5Botan11OctetStringeOERKS0_

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb240`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57c90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 00492434 ["INT_ADD", "register:40f0:8", ["const:492434:8", "const:4:8"]]
+ 004b52cc ["INT_ADD", "register:40f0:8", ["const:4b52cc:8", "const:4:8"]]
~~~


### [`004925cc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/004925cc.md) → [`004b5464`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5464.md) _ZN5BotanneERKNS_11OctetStringES2_

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdbd60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c587b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c587b0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004925d4 ["INT_ADD", "register:40f0:8", ["const:4925d4:8", "const:4:8"]]
+ 004b546c ["INT_ADD", "register:40f0:8", ["const:4b546c:8", "const:4:8"]]
~~~


### [`00493288`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/00493288.md) → [`004b6120`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b6120.md) _ZN5Botan13base64_decodeEPKcmb

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00490630`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`0051d614`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdbda0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbda0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004b34c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`005404ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c587f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c587f0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004932cc ["INT_ADD", "register:40f0:8", ["const:4932cc:8", "const:4:8"]]
+ 004b6164 ["INT_ADD", "register:40f0:8", ["const:4b6164:8", "const:4:8"]]
- 004932e0 ["INT_ADD", "register:40f0:8", ["const:4932e0:8", "const:4:8"]]
+ 004b6178 ["INT_ADD", "register:40f0:8", ["const:4b6178:8", "const:4:8"]]
- 004932f8 ["INT_ADD", "register:40f0:8", ["const:4932f8:8", "const:4:8"]]
+ 004b6190 ["INT_ADD", "register:40f0:8", ["const:4b6190:8", "const:4:8"]]
~~~


### [`00493354`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/00493354.md) → [`004b61ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b61ec.md) _ZN5Botan13base64_decodeERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdbdb0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbdb0.md) · 呼出先 3件 [`00490630`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`0051d614`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdbda0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbda0.md)
- 新版 呼出元 1件 [`00c58800`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58800.md) · 呼出先 3件 [`004b34c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`005404ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c587f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c587f0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004933a8 ["INT_ADD", "register:40f0:8", ["const:4933a8:8", "const:4:8"]]
+ 004b6240 ["INT_ADD", "register:40f0:8", ["const:4b6240:8", "const:4:8"]]
- 004933bc ["INT_ADD", "register:40f0:8", ["const:4933bc:8", "const:4:8"]]
+ 004b6254 ["INT_ADD", "register:40f0:8", ["const:4b6254:8", "const:4:8"]]
- 004933d4 ["INT_ADD", "register:40f0:8", ["const:4933d4:8", "const:4:8"]]
+ 004b626c ["INT_ADD", "register:40f0:8", ["const:4b626c:8", "const:4:8"]]
~~~


### [`00494544`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494544.md) → [`004b73dc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b73dc.md) _ZN5Botan6BigInt13encode_lockedERKS0_NS0_4BaseE

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00490630`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00bdbaf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbaf0.md) [`00bdbb00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004b34c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00c58540`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58540.md) [`00c58550`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58550.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 00494560 ["INT_ADD", "register:40f0:8", ["const:494560:8", "const:4:8"]]
+ 004b73f8 ["INT_ADD", "register:40f0:8", ["const:4b73f8:8", "const:4:8"]]
- 0049456c ["INT_ADD", "register:40f0:8", ["const:49456c:8", "const:4:8"]]
+ 004b7404 ["INT_ADD", "register:40f0:8", ["const:4b7404:8", "const:4:8"]]
- 0049457c ["INT_ADD", "register:40f0:8", ["const:49457c:8", "const:4:8"]]
+ 004b7414 ["INT_ADD", "register:40f0:8", ["const:4b7414:8", "const:4:8"]]
~~~


### [`004945e8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/004945e8.md) → [`004b7480`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7480.md) _ZN5Botan6BigInt11encode_1363ERKS0_m

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00490630`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00bdbe10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004b34c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00c58860`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58860.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 00494600 ["INT_ADD", "register:40f0:8", ["const:494600:8", "const:4:8"]]
+ 004b7498 ["INT_ADD", "register:40f0:8", ["const:4b7498:8", "const:4:8"]]
- 00494610 ["INT_ADD", "register:40f0:8", ["const:494610:8", "const:4:8"]]
+ 004b74a8 ["INT_ADD", "register:40f0:8", ["const:4b74a8:8", "const:4:8"]]
~~~


### [`004947cc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/004947cc.md) → [`004b7664`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7664.md) _ZN5Botan6BigInt28encode_fixed_length_int_pairERKS0_S2_m

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00490630`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00bdbe10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004b34c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00c58860`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58860.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004947f4 ["INT_ADD", "register:40f0:8", ["const:4947f4:8", "const:4:8"]]
+ 004b768c ["INT_ADD", "register:40f0:8", ["const:4b768c:8", "const:4:8"]]
- 00494804 ["INT_ADD", "register:40f0:8", ["const:494804:8", "const:4:8"]]
+ 004b769c ["INT_ADD", "register:40f0:8", ["const:4b769c:8", "const:4:8"]]
- 00494818 ["INT_ADD", "register:40f0:8", ["const:494818:8", "const:4:8"]]
+ 004b76b0 ["INT_ADD", "register:40f0:8", ["const:4b76b0:8", "const:4:8"]]
~~~


### [`00494b6c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494b6c.md) → [`004b7a04`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7a04.md) _ZN5Botan17hex_decode_lockedEPKcmb

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00490630`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`0051d614`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdbc90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004b34c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`005404ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c586e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c586e0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 00494b98 ["INT_ADD", "register:40f0:8", ["const:494b98:8", "const:4:8"]]
+ 004b7a30 ["INT_ADD", "register:40f0:8", ["const:4b7a30:8", "const:4:8"]]
- 00494bac ["INT_ADD", "register:40f0:8", ["const:494bac:8", "const:4:8"]]
+ 004b7a44 ["INT_ADD", "register:40f0:8", ["const:4b7a44:8", "const:4:8"]]
- 00494bc4 ["INT_ADD", "register:40f0:8", ["const:494bc4:8", "const:4:8"]]
+ 004b7a5c ["INT_ADD", "register:40f0:8", ["const:4b7a5c:8", "const:4:8"]]
~~~


### [`004958dc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004958dc.md) → [`004b8774`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8774.md) FUN_004b8774

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`004950f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004950f0.md) [`004958dc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004958dc.md) [`00495e3c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495e3c.md) [`00496ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496ee0.md) [`00497068`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497068.md) · 呼出先 1件 [`004958dc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004958dc.md)
- 新版 呼出元 9件 [`004b7f88`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7f88.md) [`004b8774`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8774.md) [`004b8cd4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8cd4.md) [`004b9d78`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9d78.md) [`004b9f00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9f00.md) · 呼出先 1件 [`004b8774`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8774.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 00495904 ["INT_ADD", "register:40f0:8", ["const:495904:8", "const:4:8"]]
+ 004b879c ["INT_ADD", "register:40f0:8", ["const:4b879c:8", "const:4:8"]]
~~~


### [`00496564`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496564.md) → [`004b93fc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b93fc.md) _ZN5Botan6BigIntrSEm

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdbde0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbde0.md) · 呼出先 1件 [`00496d60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496d60.md)
- 新版 呼出元 1件 [`00c58830`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58830.md) · 呼出先 1件 [`004b9bf8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9bf8.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004965ac ["INT_ADD", "register:40f0:8", ["const:4965ac:8", "const:4:8"]]
+ 004b9444 ["INT_ADD", "register:40f0:8", ["const:4b9444:8", "const:4:8"]]
~~~


### [`00496c30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496c30.md) → [`004b9ac8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9ac8.md) _ZN5Botan6BigIntlSEm

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdbdc0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbdc0.md) · 呼出先 3件 [`0051da48`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md) [`00bdb0f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb240`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00c58810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58810.md) · 呼出先 3件 [`005408e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md) [`00c57b40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 00496cc0 ["INT_ADD", "register:40f0:8", ["const:496cc0:8", "const:4:8"]]
+ 004b9b58 ["INT_ADD", "register:40f0:8", ["const:4b9b58:8", "const:4:8"]]
- 00496cfc ["INT_ADD", "register:40f0:8", ["const:496cfc:8", "const:4:8"]]
+ 004b9b94 ["INT_ADD", "register:40f0:8", ["const:4b9b94:8", "const:4:8"]]
- 00496d0c ["INT_ADD", "register:40f0:8", ["const:496d0c:8", "const:4:8"]]
+ 004b9ba4 ["INT_ADD", "register:40f0:8", ["const:4b9ba4:8", "const:4:8"]]
~~~


### [`00496d60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496d60.md) → [`004b9bf8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9bf8.md) FUN_004b9bf8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00496564`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496564.md) [`004b6640`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b6/004b6640.md) [`004b77d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b7/004b77d0.md) [`004ba430`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ba/004ba430.md) [`004bcf24`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bcf24.md) · 呼出先 2件 [`00bdb0f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb240`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 5件 [`004b93fc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b93fc.md) [`004d94d8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d9/004d94d8.md) [`004da668`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004da/004da668.md) [`004dd2c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dd/004dd2c8.md) [`004dfdbc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004dfdbc.md) · 呼出先 2件 [`00c57b40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 00496dc8 ["INT_ADD", "register:40f0:8", ["const:496dc8:8", "const:4:8"]]
+ 004b9c60 ["INT_ADD", "register:40f0:8", ["const:4b9c60:8", "const:4:8"]]
- 00496e08 ["INT_ADD", "register:40f0:8", ["const:496e08:8", "const:4:8"]]
+ 004b9ca0 ["INT_ADD", "register:40f0:8", ["const:4b9ca0:8", "const:4:8"]]
~~~


### [`00497bf4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497bf4.md) → [`004baa8c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004baa8c.md) _ZN5Botan6BigInt14random_integerERNS_21RandomNumberGeneratorERKS0_S4_

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdbeb0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbeb0.md) · 呼出先 2件 [`00bdbcd0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcd0.md) [`00bdbea0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbea0.md)
- 新版 呼出元 1件 [`00c58900`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58900.md) · 呼出先 2件 [`00c58720`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58720.md) [`00c588f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c588f0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 00497cb0 ["INT_ADD", "register:40f0:8", ["const:497cb0:8", "const:4:8"]]
+ 004bab48 ["INT_ADD", "register:40f0:8", ["const:4bab48:8", "const:4:8"]]
- 00497cc0 ["INT_ADD", "register:40f0:8", ["const:497cc0:8", "const:4:8"]]
+ 004bab58 ["INT_ADD", "register:40f0:8", ["const:4bab58:8", "const:4:8"]]
- 00497cd4 ["INT_ADD", "register:40f0:8", ["const:497cd4:8", "const:4:8"]]
+ 004bab6c ["INT_ADD", "register:40f0:8", ["const:4bab6c:8", "const:4:8"]]
~~~


### [`00497d04`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497d04.md) → [`004bab9c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004bab9c.md) _ZN5Botan6BigIntC1Em

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdbad0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md) · 呼出先 1件 [`0051da48`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md)
- 新版 呼出元 1件 [`00c58520`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md) · 呼出先 1件 [`005408e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 00497d30 ["INT_ADD", "register:40f0:8", ["const:497d30:8", "const:4:8"]]
+ 004babc8 ["INT_ADD", "register:40f0:8", ["const:4babc8:8", "const:4:8"]]
~~~


### [`00497d5c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497d5c.md) → [`004babf4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004babf4.md) _ZN5Botan6BigIntC1ENS0_4SignEm

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdbdd0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbdd0.md) · 呼出先 1件 [`0051da48`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md)
- 新版 呼出元 1件 [`00c58820`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58820.md) · 呼出先 1件 [`005408e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 00497da0 ["INT_ADD", "register:40f0:8", ["const:497da0:8", "const:4:8"]]
+ 004bac38 ["INT_ADD", "register:40f0:8", ["const:4bac38:8", "const:4:8"]]
~~~


### [`00497dc8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497dc8.md) → [`004bac60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004bac60.md) _ZN5Botan6BigIntC2ERKS0_

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdbcf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcf0.md) · 呼出先 1件 [`00520804`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520804.md)
- 新版 呼出元 1件 [`00c58740`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58740.md) · 呼出先 1件 [`0054369c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054369c.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 00497e04 ["INT_ADD", "register:40f0:8", ["const:497e04:8", "const:4:8"]]
+ 004bac9c ["INT_ADD", "register:40f0:8", ["const:4bac9c:8", "const:4:8"]]
~~~


### [`0049811c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/0049811c.md) → [`004bafb4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004bafb4.md) _ZN5Botan6BigIntC2ERNS_21RandomNumberGeneratorEmb

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdc500`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc500.md) · 呼出先 1件 [`00bdbea0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbea0.md)
- 新版 呼出元 1件 [`00c58f50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f50.md) · 呼出先 1件 [`00c588f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c588f0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 0049813c ["INT_ADD", "register:40f0:8", ["const:49813c:8", "const:4:8"]]
+ 004bafd4 ["INT_ADD", "register:40f0:8", ["const:4bafd4:8", "const:4:8"]]
~~~


### [`00498160`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498160.md) → [`004baff8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004baff8.md) _ZNK5Botan6BigInt3cmpERKS0_b

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdbcd0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcd0.md) · 呼出先 1件 [`004958dc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004958dc.md)
- 新版 呼出元 1件 [`00c58720`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58720.md) · 呼出先 1件 [`004b8774`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8774.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004981f0 ["INT_ADD", "register:40f0:8", ["const:4981f0:8", "const:4:8"]]
+ 004bb088 ["INT_ADD", "register:40f0:8", ["const:4bb088:8", "const:4:8"]]
~~~


### [`004986a4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/004986a4.md) → [`004bb53c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb53c.md) _ZN5Botan6BigInt7set_bitEm

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0051da48`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005408e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004986f4 ["INT_ADD", "register:40f0:8", ["const:4986f4:8", "const:4:8"]]
+ 004bb58c ["INT_ADD", "register:40f0:8", ["const:4bb58c:8", "const:4:8"]]
~~~


### [`00499040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499040.md) → [`004bbed8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbed8.md) FUN_004bbed8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049e3f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e3f4.md) · 呼出先 1件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`004c128c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c128c.md) · 呼出先 1件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 0049908c ["INT_ADD", "register:40f0:8", ["const:49908c:8", "const:4:8"]]
+ 004bbf24 ["INT_ADD", "register:40f0:8", ["const:4bbf24:8", "const:4:8"]]
- 0049909c ["INT_ADD", "register:40f0:8", ["const:49909c:8", "const:4:8"]]
+ 004bbf34 ["INT_ADD", "register:40f0:8", ["const:4bbf34:8", "const:4:8"]]
- 004990d8 ["INT_ADD", "register:40f0:8", ["const:4990d8:8", "const:4:8"]]
+ 004bbf70 ["INT_ADD", "register:40f0:8", ["const:4bbf70:8", "const:4:8"]]
~~~


### [`0049923c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/0049923c.md) → [`004bc0d4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc0d4.md) _ZN5Botan11BlockCipher9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00450668`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`004993a0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/004993a0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00473500`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`004bc238`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc238.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004992ac ["INT_ADD", "register:40f0:8", ["const:4992ac:8", "const:4:8"]]
+ 004bc144 ["INT_ADD", "register:40f0:8", ["const:4bc144:8", "const:4:8"]]
- 004992bc ["INT_ADD", "register:40f0:8", ["const:4992bc:8", "const:4:8"]]
+ 004bc154 ["INT_ADD", "register:40f0:8", ["const:4bc154:8", "const:4:8"]]
- 004992f8 ["INT_ADD", "register:40f0:8", ["const:4992f8:8", "const:4:8"]]
+ 004bc190 ["INT_ADD", "register:40f0:8", ["const:4bc190:8", "const:4:8"]]
~~~


### [`004993a0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/004993a0.md) → [`004bc238`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc238.md) FUN_004bc238

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0049923c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/0049923c.md) · 呼出先 4件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0051dea4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dea4.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdbee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbee0.md)
- 新版 呼出元 1件 [`004bc0d4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc0d4.md) · 呼出先 4件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58930`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58930.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004993f0 ["INT_ADD", "register:40f0:8", ["const:4993f0:8", "const:4:8"]]
+ 004bc288 ["INT_ADD", "register:40f0:8", ["const:4bc288:8", "const:4:8"]]
- 00499404 ["INT_ADD", "register:40f0:8", ["const:499404:8", "const:4:8"]]
+ 004bc29c ["INT_ADD", "register:40f0:8", ["const:4bc29c:8", "const:4:8"]]
- 00499420 ["INT_ADD", "register:40f0:8", ["const:499420:8", "const:4:8"]]
+ 004bc2b8 ["INT_ADD", "register:40f0:8", ["const:4bc2b8:8", "const:4:8"]]
~~~


### [`00499808`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499808.md) → [`004bc6a0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc6a0.md) _ZN5Botan8CBC_Mode5clearEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

~~~diff
- 00499824 ["INT_ADD", "register:40f0:8", ["const:499824:8", "const:4:8"]]
+ 004bc6bc ["INT_ADD", "register:40f0:8", ["const:4bc6bc:8", "const:4:8"]]
~~~


### [`00499aa4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499aa4.md) → [`004bc93c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc93c.md) _ZNK5Botan8CBC_Mode18update_granularityEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

~~~diff
- 00499ac0 ["INT_ADD", "register:40f0:8", ["const:499ac0:8", "const:4:8"]]
+ 004bc958 ["INT_ADD", "register:40f0:8", ["const:4bc958:8", "const:4:8"]]
- 00499ad4 ["INT_ADD", "register:40f0:8", ["const:499ad4:8", "const:4:8"]]
+ 004bc96c ["INT_ADD", "register:40f0:8", ["const:4bc96c:8", "const:4:8"]]
~~~


### [`0049ae90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049ae90.md) → [`004bdd28`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bdd28.md) _ZN5Botan14CBC_Decryption5resetEv

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb240`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57c90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 0049aeb4 ["INT_ADD", "register:40f0:8", ["const:49aeb4:8", "const:4:8"]]
+ 004bdd4c ["INT_ADD", "register:40f0:8", ["const:4bdd4c:8", "const:4:8"]]
~~~


### [`0049bbfc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bbfc.md) → [`004bea94`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004bea94.md) _ZN5Botan11string_joinERKNSt6__ndk16vectorINS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS5_IS7_EEEEc

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb130`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb7b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57b80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c58200`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58200.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 0049bc48 ["INT_ADD", "register:40f0:8", ["const:49bc48:8", "const:4:8"]]
+ 004beae0 ["INT_ADD", "register:40f0:8", ["const:4beae0:8", "const:4:8"]]
- 0049bc70 ["INT_ADD", "register:40f0:8", ["const:49bc70:8", "const:4:8"]]
+ 004beb08 ["INT_ADD", "register:40f0:8", ["const:4beb08:8", "const:4:8"]]
~~~


### [`0049bdc0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bdc0.md) → [`004bec58`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004bec58.md) _ZN5Botan5CPUID15bit_from_stringERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0049bfc8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bfc8.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004bee60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004bee60.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 0049be40 ["INT_ADD", "register:40f0:8", ["const:49be40:8", "const:4:8"]]
+ 004becd8 ["INT_ADD", "register:40f0:8", ["const:4becd8:8", "const:4:8"]]
- 0049bea4 ["INT_ADD", "register:40f0:8", ["const:49bea4:8", "const:4:8"]]
+ 004bed3c ["INT_ADD", "register:40f0:8", ["const:4bed3c:8", "const:4:8"]]
- 0049bef0 ["INT_ADD", "register:40f0:8", ["const:49bef0:8", "const:4:8"]]
+ 004bed88 ["INT_ADD", "register:40f0:8", ["const:4bed88:8", "const:4:8"]]
~~~


### [`0049bfc8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bfc8.md) → [`004bee60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004bee60.md) FUN_004bee60

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049bdc0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bdc0.md) · 呼出先 5件 [`00520ae8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520ae8.md) [`00bd70ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`004bec58`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004bec58.md) · 呼出先 5件 [`00543980`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543980.md) [`00c53b3c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 0049bffc ["INT_ADD", "register:40f0:8", ["const:49bffc:8", "const:4:8"]]
+ 004bee94 ["INT_ADD", "register:40f0:8", ["const:4bee94:8", "const:4:8"]]
- 0049c014 ["INT_ADD", "register:40f0:8", ["const:49c014:8", "const:4:8"]]
+ 004beeac ["INT_ADD", "register:40f0:8", ["const:4beeac:8", "const:4:8"]]
- 0049c030 ["INT_ADD", "register:40f0:8", ["const:49c030:8", "const:4:8"]]
+ 004beec8 ["INT_ADD", "register:40f0:8", ["const:4beec8:8", "const:4:8"]]
~~~


### [`0049c500`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c500.md) → [`004bf398`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf398.md) _ZNK5Botan8ECB_Mode18update_granularityEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

~~~diff
- 0049c51c ["INT_ADD", "register:40f0:8", ["const:49c51c:8", "const:4:8"]]
+ 004bf3b4 ["INT_ADD", "register:40f0:8", ["const:4bf3b4:8", "const:4:8"]]
- 0049c530 ["INT_ADD", "register:40f0:8", ["const:49c530:8", "const:4:8"]]
+ 004bf3c8 ["INT_ADD", "register:40f0:8", ["const:4bf3c8:8", "const:4:8"]]
~~~


### [`0049cd68`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049cd68.md) → [`004bfc00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bfc00.md) _ZN5Botan13EMSA_PKCS1v158raw_dataEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00490630`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004b34c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 0049cd88 ["INT_ADD", "register:40f0:8", ["const:49cd88:8", "const:4:8"]]
+ 004bfc20 ["INT_ADD", "register:40f0:8", ["const:4bfc20:8", "const:4:8"]]
- 0049cd94 ["INT_ADD", "register:40f0:8", ["const:49cd94:8", "const:4:8"]]
+ 004bfc2c ["INT_ADD", "register:40f0:8", ["const:4bfc2c:8", "const:4:8"]]
- 0049cda8 ["INT_ADD", "register:40f0:8", ["const:49cda8:8", "const:4:8"]]
+ 004bfc40 ["INT_ADD", "register:40f0:8", ["const:4bfc40:8", "const:4:8"]]
~~~


### [`0049cdcc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049cdcc.md) → [`004bfc64`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bfc64.md) FUN_004bfc64

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0049ef6c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049ef6c.md) · 呼出先 1件 [`00490630`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md)
- 新版 呼出元 1件 [`004c1e04`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c1e04.md) · 呼出先 1件 [`004b34c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 0049cde8 ["INT_ADD", "register:40f0:8", ["const:49cde8:8", "const:4:8"]]
+ 004bfc80 ["INT_ADD", "register:40f0:8", ["const:4bfc80:8", "const:4:8"]]
- 0049cdf4 ["INT_ADD", "register:40f0:8", ["const:49cdf4:8", "const:4:8"]]
+ 004bfc8c ["INT_ADD", "register:40f0:8", ["const:4bfc8c:8", "const:4:8"]]
- 0049ce08 ["INT_ADD", "register:40f0:8", ["const:49ce08:8", "const:4:8"]]
+ 004bfca0 ["INT_ADD", "register:40f0:8", ["const:4bfca0:8", "const:4:8"]]
~~~


### [`0049d82c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d82c.md) → [`004c06c4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c06c4.md) FUN_004c06c4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004daaa4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004da/004daaa4.md) [`00859898`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md) · 呼出先 1件 [`00bdb200`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 2件 [`004fd93c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd93c.md) [`0088c830`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 1件 [`00c57c50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 0049d898 ["INT_ADD", "register:40f0:8", ["const:49d898:8", "const:4:8"]]
+ 004c0730 ["INT_ADD", "register:40f0:8", ["const:4c0730:8", "const:4:8"]]
~~~


### [`0049d8dc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d8dc.md) → [`004c0774`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0774.md) FUN_004c0774

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0049d2b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d2b0.md) [`0049f624`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049f624.md) · 呼出先 5件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bdbf80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf80.md)
- 新版 呼出元 2件 [`004c0148`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0148.md) [`004c24bc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c24bc.md) · 呼出先 5件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c589d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589d0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 0049d928 ["INT_ADD", "register:40f0:8", ["const:49d928:8", "const:4:8"]]
+ 004c07c0 ["INT_ADD", "register:40f0:8", ["const:4c07c0:8", "const:4:8"]]
- 0049d934 ["INT_ADD", "register:40f0:8", ["const:49d934:8", "const:4:8"]]
+ 004c07cc ["INT_ADD", "register:40f0:8", ["const:4c07cc:8", "const:4:8"]]
- 0049d944 ["INT_ADD", "register:40f0:8", ["const:49d944:8", "const:4:8"]]
+ 004c07dc ["INT_ADD", "register:40f0:8", ["const:4c07dc:8", "const:4:8"]]
~~~


### [`0049dba0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049dba0.md) → [`004c0a38`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0a38.md) FUN_004c0a38

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0050a638`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050a638.md) [`0050b45c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050b/0050b45c.md) · 呼出先 1件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0052d4d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d4d0.md) [`0052e2f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052e2f4.md) · 呼出先 1件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 0049dbbc ["INT_ADD", "register:40f0:8", ["const:49dbbc:8", "const:4:8"]]
+ 004c0a54 ["INT_ADD", "register:40f0:8", ["const:4c0a54:8", "const:4:8"]]
~~~


### [`0049e688`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e688.md) → [`004c1520`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c1520.md) _ZN5Botan17EMSA_PKCS1v15_Raw6updateEPKhm

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051d614`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb0f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005404ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57b40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 0049e6c0 ["INT_ADD", "register:40f0:8", ["const:49e6c0:8", "const:4:8"]]
+ 004c1558 ["INT_ADD", "register:40f0:8", ["const:4c1558:8", "const:4:8"]]
~~~


### [`0049e9d8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e9d8.md) → [`004c1870`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c1870.md) _ZN5Botan4PSSR8raw_dataEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00490630`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004b34c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 0049e9f8 ["INT_ADD", "register:40f0:8", ["const:49e9f8:8", "const:4:8"]]
+ 004c1890 ["INT_ADD", "register:40f0:8", ["const:4c1890:8", "const:4:8"]]
- 0049ea04 ["INT_ADD", "register:40f0:8", ["const:49ea04:8", "const:4:8"]]
+ 004c189c ["INT_ADD", "register:40f0:8", ["const:4c189c:8", "const:4:8"]]
- 0049ea18 ["INT_ADD", "register:40f0:8", ["const:49ea18:8", "const:4:8"]]
+ 004c18b0 ["INT_ADD", "register:40f0:8", ["const:4c18b0:8", "const:4:8"]]
~~~


### [`004a0414`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0414.md) → [`004c32ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c32ac.md) _ZN5Botan15Entropy_Sources10add_sourceENSt6__ndk110unique_ptrINS_14Entropy_SourceENS1_14default_deleteIS3_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdbfe0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbfe0.md) · 呼出先 5件 [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00520d70`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d70.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00c58a30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a30.md) · 呼出先 5件 [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00543c08`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c08.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a0498 ["INT_ADD", "register:40f0:8", ["const:4a0498:8", "const:4:8"]]
+ 004c3330 ["INT_ADD", "register:40f0:8", ["const:4c3330:8", "const:4:8"]]
- 004a04d0 ["INT_ADD", "register:40f0:8", ["const:4a04d0:8", "const:4:8"]]
+ 004c3368 ["INT_ADD", "register:40f0:8", ["const:4c3368:8", "const:4:8"]]
- 004a04e4 ["INT_ADD", "register:40f0:8", ["const:4a04e4:8", "const:4:8"]]
+ 004c337c ["INT_ADD", "register:40f0:8", ["const:4c337c:8", "const:4:8"]]
~~~


### [`004a050c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a050c.md) → [`004c33a4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c33a4.md) _ZNK5Botan15Entropy_Sources15enabled_sourcesEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a05b0 ["INT_ADD", "register:40f0:8", ["const:4a05b0:8", "const:4:8"]]
+ 004c3448 ["INT_ADD", "register:40f0:8", ["const:4c3448:8", "const:4:8"]]
- 004a0618 ["INT_ADD", "register:40f0:8", ["const:4a0618:8", "const:4:8"]]
+ 004c34b0 ["INT_ADD", "register:40f0:8", ["const:4c34b0:8", "const:4:8"]]
- 004a065c ["INT_ADD", "register:40f0:8", ["const:4a065c:8", "const:4:8"]]
+ 004c34f4 ["INT_ADD", "register:40f0:8", ["const:4c34f4:8", "const:4:8"]]
~~~


### [`004a0754`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0754.md) → [`004c35ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c35ec.md) _ZN5Botan15Entropy_Sources4pollERNS_21RandomNumberGeneratorEmNSt6__ndk16chrono8durationIxNS3_5ratioILl1ELl1000EEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb730`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb730.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58180.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a0778 ["INT_ADD", "register:40f0:8", ["const:4a0778:8", "const:4:8"]]
+ 004c3610 ["INT_ADD", "register:40f0:8", ["const:4c3610:8", "const:4:8"]]
- 004a07a8 ["INT_ADD", "register:40f0:8", ["const:4a07a8:8", "const:4:8"]]
+ 004c3640 ["INT_ADD", "register:40f0:8", ["const:4c3640:8", "const:4:8"]]
- 004a07b8 ["INT_ADD", "register:40f0:8", ["const:4a07b8:8", "const:4:8"]]
+ 004c3650 ["INT_ADD", "register:40f0:8", ["const:4c3650:8", "const:4:8"]]
~~~


### [`004a07f8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a07f8.md) → [`004c3690`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3690.md) _ZN5Botan15Entropy_Sources9poll_justERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a0854 ["INT_ADD", "register:40f0:8", ["const:4a0854:8", "const:4:8"]]
+ 004c36ec ["INT_ADD", "register:40f0:8", ["const:4c36ec:8", "const:4:8"]]
- 004a0860 ["INT_ADD", "register:40f0:8", ["const:4a0860:8", "const:4:8"]]
+ 004c36f8 ["INT_ADD", "register:40f0:8", ["const:4c36f8:8", "const:4:8"]]
- 004a088c ["INT_ADD", "register:40f0:8", ["const:4a088c:8", "const:4:8"]]
+ 004c3724 ["INT_ADD", "register:40f0:8", ["const:4c3724:8", "const:4:8"]]
~~~


### [`004a0978`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0978.md) → [`004c3810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3810.md) FUN_004c3810

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`004daaa4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004da/004daaa4.md) [`0086a350`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086a/0086a350.md) [`0086b704`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 1件 [`00bdb200`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 3件 [`004fd93c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd93c.md) [`0089d484`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089d/0089d484.md) [`0089e838`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 1件 [`00c57c50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a09e4 ["INT_ADD", "register:40f0:8", ["const:4a09e4:8", "const:4:8"]]
+ 004c387c ["INT_ADD", "register:40f0:8", ["const:4c387c:8", "const:4:8"]]
~~~


### [`004a0be8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0be8.md) → [`004c3a80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3a80.md) FUN_004c3a80

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a0c34 ["INT_ADD", "register:40f0:8", ["const:4a0c34:8", "const:4:8"]]
+ 004c3acc ["INT_ADD", "register:40f0:8", ["const:4c3acc:8", "const:4:8"]]
~~~


### [`004a0fc4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0fc4.md) → [`004c3e5c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3e5c.md) FUN_004c3e5c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004a0c64`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0c64.md) · 呼出先 1件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`004c3afc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3afc.md) · 呼出先 1件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a1010 ["INT_ADD", "register:40f0:8", ["const:4a1010:8", "const:4:8"]]
+ 004c3ea8 ["INT_ADD", "register:40f0:8", ["const:4c3ea8:8", "const:4:8"]]
~~~


### [`004a17a0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a17a0.md) → [`004c4638`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4638.md) _ZN5Botan19StreamCipher_Filter5writeEPKhm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a17e4 ["INT_ADD", "register:40f0:8", ["const:4a17e4:8", "const:4:8"]]
+ 004c467c ["INT_ADD", "register:40f0:8", ["const:4c467c:8", "const:4:8"]]
- 004a17fc ["INT_ADD", "register:40f0:8", ["const:4a17fc:8", "const:4:8"]]
+ 004c4694 ["INT_ADD", "register:40f0:8", ["const:4c4694:8", "const:4:8"]]
~~~


### [`004a28b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a28b8.md) → [`004c5750`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5750.md) _ZN5Botan15Buffered_Filter5writeEPKhm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc060.md) · 呼出先 1件 [`00bdb0f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00c58ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ab0.md) · 呼出先 1件 [`00c57b40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a2918 ["INT_ADD", "register:40f0:8", ["const:4a2918:8", "const:4:8"]]
+ 004c57b0 ["INT_ADD", "register:40f0:8", ["const:4c57b0:8", "const:4:8"]]
- 004a2964 ["INT_ADD", "register:40f0:8", ["const:4a2964:8", "const:4:8"]]
+ 004c57fc ["INT_ADD", "register:40f0:8", ["const:4c57fc:8", "const:4:8"]]
- 004a2980 ["INT_ADD", "register:40f0:8", ["const:4a2980:8", "const:4:8"]]
+ 004c5818 ["INT_ADD", "register:40f0:8", ["const:4c5818:8", "const:4:8"]]
~~~


### [`004a3114`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3114.md) → [`004c5fac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5fac.md) _ZN5Botan18Cipher_Mode_Filter14buffered_blockEPKhm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc080`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc080.md) · 呼出先 2件 [`0051d614`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`005204e8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/005204e8.md)
- 新版 呼出元 1件 [`00c58ad0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ad0.md) · 呼出先 2件 [`005404ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00543380`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543380.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a3144 ["INT_ADD", "register:40f0:8", ["const:4a3144:8", "const:4:8"]]
+ 004c5fdc ["INT_ADD", "register:40f0:8", ["const:4c5fdc:8", "const:4:8"]]
- 004a315c ["INT_ADD", "register:40f0:8", ["const:4a315c:8", "const:4:8"]]
+ 004c5ff4 ["INT_ADD", "register:40f0:8", ["const:4c5ff4:8", "const:4:8"]]
- 004a3178 ["INT_ADD", "register:40f0:8", ["const:4a3178:8", "const:4:8"]]
+ 004c6010 ["INT_ADD", "register:40f0:8", ["const:4c6010:8", "const:4:8"]]
~~~


### [`004a38b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a38b0.md) → [`004c6748`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6748.md) _ZN5Botan15DataSink_StreamD0Ev

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdc0e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58b30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b30.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a38c0 ["INT_ADD", "register:40f0:8", ["const:4a38c0:8", "const:4:8"]]
+ 004c6758 ["INT_ADD", "register:40f0:8", ["const:4c6758:8", "const:4:8"]]
~~~


### [`004a38d4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a38d4.md) → [`004c676c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c676c.md) _ZN5Botan6Filter4sendEPKhm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc0f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0f0.md) · 呼出先 2件 [`0051d614`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb0f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00c58b40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b40.md) · 呼出先 2件 [`005404ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57b40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a3940 ["INT_ADD", "register:40f0:8", ["const:4a3940:8", "const:4:8"]]
+ 004c67d8 ["INT_ADD", "register:40f0:8", ["const:4c67d8:8", "const:4:8"]]
- 004a395c ["INT_ADD", "register:40f0:8", ["const:4a395c:8", "const:4:8"]]
+ 004c67f4 ["INT_ADD", "register:40f0:8", ["const:4c67f4:8", "const:4:8"]]
- 004a39a8 ["INT_ADD", "register:40f0:8", ["const:4a39a8:8", "const:4:8"]]
+ 004c6840 ["INT_ADD", "register:40f0:8", ["const:4c6840:8", "const:4:8"]]
~~~


### [`004a3a0c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3a0c.md) → [`004c68a4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c68a4.md) _ZN5Botan6Filter7new_msgEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc100`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc100.md) · 呼出先 1件 [`00bdc100`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc100.md)
- 新版 呼出元 1件 [`00c58b50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b50.md) · 呼出先 1件 [`00c58b50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b50.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a3a24 ["INT_ADD", "register:40f0:8", ["const:4a3a24:8", "const:4:8"]]
+ 004c68bc ["INT_ADD", "register:40f0:8", ["const:4c68bc:8", "const:4:8"]]
- 004a3a54 ["INT_ADD", "register:40f0:8", ["const:4a3a54:8", "const:4:8"]]
+ 004c68ec ["INT_ADD", "register:40f0:8", ["const:4c68ec:8", "const:4:8"]]
~~~


### [`004a3a6c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3a6c.md) → [`004c6904`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6904.md) _ZN5Botan6Filter10finish_msgEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc110`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc110.md) · 呼出先 1件 [`00bdc110`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc110.md)
- 新版 呼出元 1件 [`00c58b60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b60.md) · 呼出先 1件 [`00c58b60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b60.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a3a84 ["INT_ADD", "register:40f0:8", ["const:4a3a84:8", "const:4:8"]]
+ 004c691c ["INT_ADD", "register:40f0:8", ["const:4c691c:8", "const:4:8"]]
- 004a3ab4 ["INT_ADD", "register:40f0:8", ["const:4a3ab4:8", "const:4:8"]]
+ 004c694c ["INT_ADD", "register:40f0:8", ["const:4c694c:8", "const:4:8"]]
~~~


### [`004a48d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a48d0.md) → [`004c7768`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7768.md) _ZN5Botan10get_cipherERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKNS_11OctetStringESB_NS_10Cipher_DirE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdc120`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc120.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58b70`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b70.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a48ec ["INT_ADD", "register:40f0:8", ["const:4a48ec:8", "const:4:8"]]
+ 004c7784 ["INT_ADD", "register:40f0:8", ["const:4c7784:8", "const:4:8"]]
- 004a4900 ["INT_ADD", "register:40f0:8", ["const:4a4900:8", "const:4:8"]]
+ 004c7798 ["INT_ADD", "register:40f0:8", ["const:4c7798:8", "const:4:8"]]
- 004a4920 ["INT_ADD", "register:40f0:8", ["const:4a4920:8", "const:4:8"]]
+ 004c77b8 ["INT_ADD", "register:40f0:8", ["const:4c77b8:8", "const:4:8"]]
~~~


### [`004a4938`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4938.md) → [`004c77d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c77d0.md) _ZN5Botan10get_cipherERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKNS_11OctetStringENS_10Cipher_DirE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdc120`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc120.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58b70`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b70.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a494c ["INT_ADD", "register:40f0:8", ["const:4a494c:8", "const:4:8"]]
+ 004c77e4 ["INT_ADD", "register:40f0:8", ["const:4c77e4:8", "const:4:8"]]
- 004a4960 ["INT_ADD", "register:40f0:8", ["const:4a4960:8", "const:4:8"]]
+ 004c77f8 ["INT_ADD", "register:40f0:8", ["const:4c77f8:8", "const:4:8"]]
~~~


### [`004a4a98`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4a98.md) → [`004c7930`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7930.md) _ZNK5Botan11SecureQueue4peekEPhmm

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdc1b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1b0.md) · 呼出先 1件 [`00bdb0f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00c58c00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c00.md) · 呼出先 1件 [`00c57b40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a4b30 ["INT_ADD", "register:40f0:8", ["const:4a4b30:8", "const:4:8"]]
+ 004c79c8 ["INT_ADD", "register:40f0:8", ["const:4c79c8:8", "const:4:8"]]
- 004a4b88 ["INT_ADD", "register:40f0:8", ["const:4a4b88:8", "const:4:8"]]
+ 004c7a20 ["INT_ADD", "register:40f0:8", ["const:4c7a20:8", "const:4:8"]]
~~~


### [`004a4d4c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4d4c.md) → [`004c7be4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7be4.md) FUN_004c7be4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0050d8f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d8f4.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053078c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053078c.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a4d68 ["INT_ADD", "register:40f0:8", ["const:4a4d68:8", "const:4:8"]]
+ 004c7c00 ["INT_ADD", "register:40f0:8", ["const:4c7c00:8", "const:4:8"]]
~~~


### [`004a4d88`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4d88.md) → [`004c7c20`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7c20.md) FUN_004c7c20

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004a5940`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5940.md) · 呼出先 2件 [`0050d8f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d8f4.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`004c87d8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c87d8.md) · 呼出先 2件 [`0053078c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053078c.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a4db4 ["INT_ADD", "register:40f0:8", ["const:4a4db4:8", "const:4:8"]]
+ 004c7c4c ["INT_ADD", "register:40f0:8", ["const:4c7c4c:8", "const:4:8"]]
- 004a4dbc ["INT_ADD", "register:40f0:8", ["const:4a4dbc:8", "const:4:8"]]
+ 004c7c54 ["INT_ADD", "register:40f0:8", ["const:4c7c54:8", "const:4:8"]]
- 004a4e70 ["INT_ADD", "register:40f0:8", ["const:4a4e70:8", "const:4:8"]]
+ 004c7d08 ["INT_ADD", "register:40f0:8", ["const:4c7d08:8", "const:4:8"]]
~~~


### [`004a5238`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5238.md) → [`004c80d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c80d0.md) FUN_004c80d0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00521954`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521954.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005447ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/005447ec.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a5254 ["INT_ADD", "register:40f0:8", ["const:4a5254:8", "const:4:8"]]
+ 004c80ec ["INT_ADD", "register:40f0:8", ["const:4c80ec:8", "const:4:8"]]
~~~


### [`004a5274`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5274.md) → [`004c810c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c810c.md) _ZN5Botan4PipeD2Ev

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdc1e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1e0.md) · 呼出先 3件 [`00521954`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521954.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdc1d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1d0.md)
- 新版 呼出元 1件 [`00c58c30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c30.md) · 呼出先 3件 [`005447ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/005447ec.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58c20`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c20.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a5288 ["INT_ADD", "register:40f0:8", ["const:4a5288:8", "const:4:8"]]
+ 004c8120 ["INT_ADD", "register:40f0:8", ["const:4c8120:8", "const:4:8"]]
- 004a529c ["INT_ADD", "register:40f0:8", ["const:4a529c:8", "const:4:8"]]
+ 004c8134 ["INT_ADD", "register:40f0:8", ["const:4c8134:8", "const:4:8"]]
~~~


### [`004a5374`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5374.md) → [`004c820c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c820c.md) _ZN5Botan4Pipe5resetEv

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdc1d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58c20`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c20.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a5388 ["INT_ADD", "register:40f0:8", ["const:4a5388:8", "const:4:8"]]
+ 004c8220 ["INT_ADD", "register:40f0:8", ["const:4c8220:8", "const:4:8"]]
~~~


### [`004a53a0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a53a0.md) → [`004c8238`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8238.md) _ZNK5Botan4Pipe11end_of_dataEv

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdc1f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58c40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c40.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a53ac ["INT_ADD", "register:40f0:8", ["const:4a53ac:8", "const:4:8"]]
+ 004c8244 ["INT_ADD", "register:40f0:8", ["const:4c8244:8", "const:4:8"]]
~~~


### [`004a5654`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5654.md) → [`004c84ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c84ec.md) _ZN5Botan4Pipe11process_msgEPKhm

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdc200`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc200.md) [`00bdc210`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc210.md) [`00bdc220`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc220.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58c50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c50.md) [`00c58c60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c60.md) [`00c58c70`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c70.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a5670 ["INT_ADD", "register:40f0:8", ["const:4a5670:8", "const:4:8"]]
+ 004c8508 ["INT_ADD", "register:40f0:8", ["const:4c8508:8", "const:4:8"]]
- 004a5680 ["INT_ADD", "register:40f0:8", ["const:4a5680:8", "const:4:8"]]
+ 004c8518 ["INT_ADD", "register:40f0:8", ["const:4c8518:8", "const:4:8"]]
~~~


### [`004a5acc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5acc.md) → [`004c8964`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8964.md) _ZN5Botan4Pipe11process_msgERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEE

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdc200`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc200.md) [`00bdc210`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc210.md) [`00bdc220`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc220.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58c50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c50.md) [`00c58c60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c60.md) [`00c58c70`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c70.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a5ae8 ["INT_ADD", "register:40f0:8", ["const:4a5ae8:8", "const:4:8"]]
+ 004c8980 ["INT_ADD", "register:40f0:8", ["const:4c8980:8", "const:4:8"]]
- 004a5af8 ["INT_ADD", "register:40f0:8", ["const:4a5af8:8", "const:4:8"]]
+ 004c8990 ["INT_ADD", "register:40f0:8", ["const:4c8990:8", "const:4:8"]]
~~~


### [`004a5b10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5b10.md) → [`004c89a8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c89a8.md) _ZN5Botan4Pipe11process_msgERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdc200`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc200.md) [`00bdc210`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc210.md) [`00bdc220`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc220.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58c50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c50.md) [`00c58c60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c60.md) [`00c58c70`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c70.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a5b2c ["INT_ADD", "register:40f0:8", ["const:4a5b2c:8", "const:4:8"]]
+ 004c89c4 ["INT_ADD", "register:40f0:8", ["const:4c89c4:8", "const:4:8"]]
- 004a5b3c ["INT_ADD", "register:40f0:8", ["const:4a5b3c:8", "const:4:8"]]
+ 004c89d4 ["INT_ADD", "register:40f0:8", ["const:4c89d4:8", "const:4:8"]]
~~~


### [`004a5b54`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5b54.md) → [`004c89ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c89ec.md) _ZN5Botan4Pipe11process_msgERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdc200`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc200.md) [`00bdc210`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc210.md) [`00bdc220`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc220.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58c50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c50.md) [`00c58c60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c60.md) [`00c58c70`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c70.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a5b80 ["INT_ADD", "register:40f0:8", ["const:4a5b80:8", "const:4:8"]]
+ 004c8a18 ["INT_ADD", "register:40f0:8", ["const:4c8a18:8", "const:4:8"]]
- 004a5b90 ["INT_ADD", "register:40f0:8", ["const:4a5b90:8", "const:4:8"]]
+ 004c8a28 ["INT_ADD", "register:40f0:8", ["const:4c8a28:8", "const:4:8"]]
~~~


### [`004a5ba8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5ba8.md) → [`004c8a40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8a40.md) _ZN5Botan4Pipe11process_msgERNS_10DataSourceE

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdc200`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc200.md) [`00bdc220`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc220.md) [`00bdc250`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc250.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58c50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c50.md) [`00c58c70`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c70.md) [`00c58ca0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ca0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a5bbc ["INT_ADD", "register:40f0:8", ["const:4a5bbc:8", "const:4:8"]]
+ 004c8a54 ["INT_ADD", "register:40f0:8", ["const:4c8a54:8", "const:4:8"]]
- 004a5bc8 ["INT_ADD", "register:40f0:8", ["const:4a5bc8:8", "const:4:8"]]
+ 004c8a60 ["INT_ADD", "register:40f0:8", ["const:4c8a60:8", "const:4:8"]]
~~~


### [`004a6a58`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6a58.md) → [`004c98f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c98f0.md) _ZN5Botan4Pipe5writeEh

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc210`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58c60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c60.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a6a80 ["INT_ADD", "register:40f0:8", ["const:4a6a80:8", "const:4:8"]]
+ 004c9918 ["INT_ADD", "register:40f0:8", ["const:4c9918:8", "const:4:8"]]
- 004a6aa4 ["INT_ADD", "register:40f0:8", ["const:4a6aa4:8", "const:4:8"]]
+ 004c993c ["INT_ADD", "register:40f0:8", ["const:4c993c:8", "const:4:8"]]
~~~


### [`004a6c04`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6c04.md) → [`004c9a9c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9a9c.md) _ZN5Botan4Pipe8read_allEm

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00490630`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`0051d614`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdc1f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1f0.md) [`00bdc270`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc270.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004b34c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`005404ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c58c40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c40.md) [`00c58cc0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58cc0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a6c2c ["INT_ADD", "register:40f0:8", ["const:4a6c2c:8", "const:4:8"]]
+ 004c9ac4 ["INT_ADD", "register:40f0:8", ["const:4c9ac4:8", "const:4:8"]]
- 004a6c38 ["INT_ADD", "register:40f0:8", ["const:4a6c38:8", "const:4:8"]]
+ 004c9ad0 ["INT_ADD", "register:40f0:8", ["const:4c9ad0:8", "const:4:8"]]
- 004a6c4c ["INT_ADD", "register:40f0:8", ["const:4a6c4c:8", "const:4:8"]]
+ 004c9ae4 ["INT_ADD", "register:40f0:8", ["const:4c9ae4:8", "const:4:8"]]
~~~


### [`004a70b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a70b0.md) → [`004c9f48`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9f48.md) _ZN5Botan4Pipe15check_availableEm

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdc1f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58c40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c40.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a70c8 ["INT_ADD", "register:40f0:8", ["const:4a70c8:8", "const:4:8"]]
+ 004c9f60 ["INT_ADD", "register:40f0:8", ["const:4c9f60:8", "const:4:8"]]
~~~


### [`004a70e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a70e0.md) → [`004c9f78`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9f78.md) _ZN5Botan4Pipe19check_available_msgEmm

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdc1f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58c40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c40.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a70f4 ["INT_ADD", "register:40f0:8", ["const:4a70f4:8", "const:4:8"]]
+ 004c9f8c ["INT_ADD", "register:40f0:8", ["const:4c9f8c:8", "const:4:8"]]
~~~


### [`004a7d10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7d10.md) → [`004caba8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004caba8.md) FUN_004caba8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a7d5c ["INT_ADD", "register:40f0:8", ["const:4a7d5c:8", "const:4:8"]]
+ 004cabf4 ["INT_ADD", "register:40f0:8", ["const:4cabf4:8", "const:4:8"]]
- 004a7d70 ["INT_ADD", "register:40f0:8", ["const:4a7d70:8", "const:4:8"]]
+ 004cac08 ["INT_ADD", "register:40f0:8", ["const:4cac08:8", "const:4:8"]]
- 004a7d78 ["INT_ADD", "register:40f0:8", ["const:4a7d78:8", "const:4:8"]]
+ 004cac10 ["INT_ADD", "register:40f0:8", ["const:4cac10:8", "const:4:8"]]
~~~


### [`004a807c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a807c.md) → [`004caf14`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004caf14.md) _ZN5Botan13Threaded_ForkD0Ev

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdc2d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc2d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58d20`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d20.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a808c ["INT_ADD", "register:40f0:8", ["const:4a808c:8", "const:4:8"]]
+ 004caf24 ["INT_ADD", "register:40f0:8", ["const:4caf24:8", "const:4:8"]]
~~~


### [`004a80c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a80c8.md) → [`004caf60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004caf60.md) FUN_004caf60

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004a7a98`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7a98.md) · 呼出先 5件 [`00521ad8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521ad8.md) [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`004ca930`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca930.md) · 呼出先 5件 [`00544970`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544970.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a810c ["INT_ADD", "register:40f0:8", ["const:4a810c:8", "const:4:8"]]
+ 004cafa4 ["INT_ADD", "register:40f0:8", ["const:4cafa4:8", "const:4:8"]]
- 004a8160 ["INT_ADD", "register:40f0:8", ["const:4a8160:8", "const:4:8"]]
+ 004caff8 ["INT_ADD", "register:40f0:8", ["const:4caff8:8", "const:4:8"]]
- 004a8174 ["INT_ADD", "register:40f0:8", ["const:4a8174:8", "const:4:8"]]
+ 004cb00c ["INT_ADD", "register:40f0:8", ["const:4cb00c:8", "const:4:8"]]
~~~


### [`004a81d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a81d0.md) → [`004cb068`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb068.md) _ZN5Botan13Threaded_Fork12thread_entryEPNS_6FilterE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004a7a98`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7a98.md) · 呼出先 5件 [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb290`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb530`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb530.md) [`00bdb630`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb630.md)
- 新版 呼出元 1件 [`004ca930`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca930.md) · 呼出先 5件 [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ce0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f80.md) [`00c58080`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58080.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a8218 ["INT_ADD", "register:40f0:8", ["const:4a8218:8", "const:4:8"]]
+ 004cb0b0 ["INT_ADD", "register:40f0:8", ["const:4cb0b0:8", "const:4:8"]]
- 004a8220 ["INT_ADD", "register:40f0:8", ["const:4a8220:8", "const:4:8"]]
+ 004cb0b8 ["INT_ADD", "register:40f0:8", ["const:4cb0b8:8", "const:4:8"]]
- 004a8234 ["INT_ADD", "register:40f0:8", ["const:4a8234:8", "const:4:8"]]
+ 004cb0cc ["INT_ADD", "register:40f0:8", ["const:4cb0cc:8", "const:4:8"]]
~~~


### [`004a8428`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8428.md) → [`004cb2c0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb2c0.md) FUN_004cb2c0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a8444 ["INT_ADD", "register:40f0:8", ["const:4a8444:8", "const:4:8"]]
+ 004cb2dc ["INT_ADD", "register:40f0:8", ["const:4cb2dc:8", "const:4:8"]]
- 004a8464 ["INT_ADD", "register:40f0:8", ["const:4a8464:8", "const:4:8"]]
+ 004cb2fc ["INT_ADD", "register:40f0:8", ["const:4cb2fc:8", "const:4:8"]]
~~~


### [`004a8478`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8478.md) → [`004cb310`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb310.md) _ZN5Botan13Threaded_Fork4sendEPKhm

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0051d614`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb0f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdc2e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc2e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005404ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57b40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c58d30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d30.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a84b0 ["INT_ADD", "register:40f0:8", ["const:4a84b0:8", "const:4:8"]]
+ 004cb348 ["INT_ADD", "register:40f0:8", ["const:4cb348:8", "const:4:8"]]
- 004a84c0 ["INT_ADD", "register:40f0:8", ["const:4a84c0:8", "const:4:8"]]
+ 004cb358 ["INT_ADD", "register:40f0:8", ["const:4cb358:8", "const:4:8"]]
- 004a8690 ["INT_ADD", "register:40f0:8", ["const:4a8690:8", "const:4:8"]]
+ 004cb528 ["INT_ADD", "register:40f0:8", ["const:4cb528:8", "const:4:8"]]
~~~


### [`004a86e8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a86e8.md) → [`004cb580`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb580.md) _ZN5Botan13Threaded_Fork20thread_delegate_workEPKhm

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdc2e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc2e0.md) · 呼出先 6件 [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb290`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb530`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb530.md) [`00bdb630`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb630.md)
- 新版 呼出元 1件 [`00c58d30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d30.md) · 呼出先 6件 [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ce0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f80.md) [`00c58080`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58080.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a872c ["INT_ADD", "register:40f0:8", ["const:4a872c:8", "const:4:8"]]
+ 004cb5c4 ["INT_ADD", "register:40f0:8", ["const:4cb5c4:8", "const:4:8"]]
- 004a8744 ["INT_ADD", "register:40f0:8", ["const:4a8744:8", "const:4:8"]]
+ 004cb5dc ["INT_ADD", "register:40f0:8", ["const:4cb5dc:8", "const:4:8"]]
- 004a8764 ["INT_ADD", "register:40f0:8", ["const:4a8764:8", "const:4:8"]]
+ 004cb5fc ["INT_ADD", "register:40f0:8", ["const:4cb5fc:8", "const:4:8"]]
~~~


### [`004a8fa8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8fa8.md) → [`004cbe40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cbe40.md) _ZN5Botan12HashFunction9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00450668`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`004a9174`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9174.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00473500`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`004cc00c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc00c.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a9038 ["INT_ADD", "register:40f0:8", ["const:4a9038:8", "const:4:8"]]
+ 004cbed0 ["INT_ADD", "register:40f0:8", ["const:4cbed0:8", "const:4:8"]]
- 004a9048 ["INT_ADD", "register:40f0:8", ["const:4a9048:8", "const:4:8"]]
+ 004cbee0 ["INT_ADD", "register:40f0:8", ["const:4cbee0:8", "const:4:8"]]
- 004a9084 ["INT_ADD", "register:40f0:8", ["const:4a9084:8", "const:4:8"]]
+ 004cbf1c ["INT_ADD", "register:40f0:8", ["const:4cbf1c:8", "const:4:8"]]
~~~


### [`004a9174`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9174.md) → [`004cc00c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc00c.md) FUN_004cc00c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004a8fa8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8fa8.md) · 呼出先 4件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0051dea4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dea4.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdbfa0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbfa0.md)
- 新版 呼出元 1件 [`004cbe40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cbe40.md) · 呼出先 4件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c589f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589f0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a91c4 ["INT_ADD", "register:40f0:8", ["const:4a91c4:8", "const:4:8"]]
+ 004cc05c ["INT_ADD", "register:40f0:8", ["const:4cc05c:8", "const:4:8"]]
- 004a91d8 ["INT_ADD", "register:40f0:8", ["const:4a91d8:8", "const:4:8"]]
+ 004cc070 ["INT_ADD", "register:40f0:8", ["const:4cc070:8", "const:4:8"]]
- 004a91f4 ["INT_ADD", "register:40f0:8", ["const:4a91f4:8", "const:4:8"]]
+ 004cc08c ["INT_ADD", "register:40f0:8", ["const:4cc08c:8", "const:4:8"]]
~~~


### [`004a92b4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a92b4.md) → [`004cc14c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc14c.md) FUN_004cc14c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049dd0c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049dd0c.md) · 呼出先 3件 [`0047c554`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`004c0ba4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0ba4.md) · 呼出先 3件 [`0049f3ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a92e4 ["INT_ADD", "register:40f0:8", ["const:4a92e4:8", "const:4:8"]]
+ 004cc17c ["INT_ADD", "register:40f0:8", ["const:4cc17c:8", "const:4:8"]]
- 004a92fc ["INT_ADD", "register:40f0:8", ["const:4a92fc:8", "const:4:8"]]
+ 004cc194 ["INT_ADD", "register:40f0:8", ["const:4cc194:8", "const:4:8"]]
- 004a9318 ["INT_ADD", "register:40f0:8", ["const:4a9318:8", "const:4:8"]]
+ 004cc1b0 ["INT_ADD", "register:40f0:8", ["const:4cc1b0:8", "const:4:8"]]
~~~


### [`004a9884`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9884.md) → [`004cc71c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc71c.md) _ZN5Botan17hex_decode_lockedERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00490630`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`0051d614`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdbc90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004b34c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`005404ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c586e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c586e0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a98c0 ["INT_ADD", "register:40f0:8", ["const:4a98c0:8", "const:4:8"]]
+ 004cc758 ["INT_ADD", "register:40f0:8", ["const:4cc758:8", "const:4:8"]]
- 004a98d4 ["INT_ADD", "register:40f0:8", ["const:4a98d4:8", "const:4:8"]]
+ 004cc76c ["INT_ADD", "register:40f0:8", ["const:4cc76c:8", "const:4:8"]]
- 004a98ec ["INT_ADD", "register:40f0:8", ["const:4a98ec:8", "const:4:8"]]
+ 004cc784 ["INT_ADD", "register:40f0:8", ["const:4cc784:8", "const:4:8"]]
~~~


### [`004a9924`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9924.md) → [`004cc7bc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc7bc.md) _ZN5Botan10hex_decodeEPKcmb

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdc300`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc300.md) · 呼出先 6件 [`0047c554`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb240`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00c58d50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d50.md) · 呼出先 6件 [`0049f3ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c57c90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004a9964 ["INT_ADD", "register:40f0:8", ["const:4a9964:8", "const:4:8"]]
+ 004cc7fc ["INT_ADD", "register:40f0:8", ["const:4cc7fc:8", "const:4:8"]]
- 004a9980 ["INT_ADD", "register:40f0:8", ["const:4a9980:8", "const:4:8"]]
+ 004cc818 ["INT_ADD", "register:40f0:8", ["const:4cc818:8", "const:4:8"]]
- 004a9998 ["INT_ADD", "register:40f0:8", ["const:4a9998:8", "const:4:8"]]
+ 004cc830 ["INT_ADD", "register:40f0:8", ["const:4cc830:8", "const:4:8"]]
~~~


### [`004aa268`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa268.md) → [`004cd100`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd100.md) _ZN5Botan4HMAC5clearEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc330`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc330.md) · 呼出先 2件 [`0051dca0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dca0.md) [`00bdb240`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00c58d80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d80.md) · 呼出先 2件 [`00540b38`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540b38.md) [`00c57c90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004aa284 ["INT_ADD", "register:40f0:8", ["const:4aa284:8", "const:4:8"]]
+ 004cd11c ["INT_ADD", "register:40f0:8", ["const:4cd11c:8", "const:4:8"]]
- 004aa29c ["INT_ADD", "register:40f0:8", ["const:4aa29c:8", "const:4:8"]]
+ 004cd134 ["INT_ADD", "register:40f0:8", ["const:4cd134:8", "const:4:8"]]
- 004aa2ac ["INT_ADD", "register:40f0:8", ["const:4aa2ac:8", "const:4:8"]]
+ 004cd144 ["INT_ADD", "register:40f0:8", ["const:4cd144:8", "const:4:8"]]
~~~


### [`004aa624`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa624.md) → [`004cd4bc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd4bc.md) _ZN5Botan3KDF6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdc360`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc360.md) · 呼出先 4件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdbef0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbef0.md)
- 新版 呼出元 1件 [`00c58db0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58db0.md) · 呼出先 4件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58940`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58940.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004aa66c ["INT_ADD", "register:40f0:8", ["const:4aa66c:8", "const:4:8"]]
+ 004cd504 ["INT_ADD", "register:40f0:8", ["const:4cd504:8", "const:4:8"]]
- 004aa678 ["INT_ADD", "register:40f0:8", ["const:4aa678:8", "const:4:8"]]
+ 004cd510 ["INT_ADD", "register:40f0:8", ["const:4cd510:8", "const:4:8"]]
- 004aa688 ["INT_ADD", "register:40f0:8", ["const:4aa688:8", "const:4:8"]]
+ 004cd520 ["INT_ADD", "register:40f0:8", ["const:4cd520:8", "const:4:8"]]
~~~


### [`004aa8b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa8b0.md) → [`004cd748`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd748.md) _ZN5Botan3KDF9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00450668`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`004aa9d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa9d0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00473500`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`004cd868`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd868.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004aa8fc ["INT_ADD", "register:40f0:8", ["const:4aa8fc:8", "const:4:8"]]
+ 004cd794 ["INT_ADD", "register:40f0:8", ["const:4cd794:8", "const:4:8"]]
- 004aa90c ["INT_ADD", "register:40f0:8", ["const:4aa90c:8", "const:4:8"]]
+ 004cd7a4 ["INT_ADD", "register:40f0:8", ["const:4cd7a4:8", "const:4:8"]]
- 004aa948 ["INT_ADD", "register:40f0:8", ["const:4aa948:8", "const:4:8"]]
+ 004cd7e0 ["INT_ADD", "register:40f0:8", ["const:4cd7e0:8", "const:4:8"]]
~~~


### [`004aa9d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa9d0.md) → [`004cd868`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd868.md) FUN_004cd868

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004aa8b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa8b0.md) · 呼出先 4件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0051dea4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dea4.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc360`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc360.md)
- 新版 呼出元 1件 [`004cd748`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd748.md) · 呼出先 4件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58db0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58db0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004aaa20 ["INT_ADD", "register:40f0:8", ["const:4aaa20:8", "const:4:8"]]
+ 004cd8b8 ["INT_ADD", "register:40f0:8", ["const:4cd8b8:8", "const:4:8"]]
- 004aaa34 ["INT_ADD", "register:40f0:8", ["const:4aaa34:8", "const:4:8"]]
+ 004cd8cc ["INT_ADD", "register:40f0:8", ["const:4cd8cc:8", "const:4:8"]]
- 004aaa4c ["INT_ADD", "register:40f0:8", ["const:4aaa4c:8", "const:4:8"]]
+ 004cd8e4 ["INT_ADD", "register:40f0:8", ["const:4cd8e4:8", "const:4:8"]]
~~~


### [`004ab178`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab178.md) → [`004ce010`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce010.md) _ZNK5Botan16PK_Encryptor_EME18maximum_input_sizeEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

~~~diff
- 004ab18c ["INT_ADD", "register:40f0:8", ["const:4ab18c:8", "const:4:8"]]
+ 004ce024 ["INT_ADD", "register:40f0:8", ["const:4ce024:8", "const:4:8"]]
~~~


### [`004ab6ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab6ac.md) → [`004ce544`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce544.md) _ZN5Botan25MessageAuthenticationCode9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00450668`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`004ab810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab810.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00473500`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`004ce6a8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce6a8.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004ab71c ["INT_ADD", "register:40f0:8", ["const:4ab71c:8", "const:4:8"]]
+ 004ce5b4 ["INT_ADD", "register:40f0:8", ["const:4ce5b4:8", "const:4:8"]]
- 004ab72c ["INT_ADD", "register:40f0:8", ["const:4ab72c:8", "const:4:8"]]
+ 004ce5c4 ["INT_ADD", "register:40f0:8", ["const:4ce5c4:8", "const:4:8"]]
- 004ab768 ["INT_ADD", "register:40f0:8", ["const:4ab768:8", "const:4:8"]]
+ 004ce600 ["INT_ADD", "register:40f0:8", ["const:4ce600:8", "const:4:8"]]
~~~


### [`004ab810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab810.md) → [`004ce6a8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce6a8.md) FUN_004ce6a8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004ab6ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab6ac.md) · 呼出先 4件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0051dea4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dea4.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc040.md)
- 新版 呼出元 1件 [`004ce544`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce544.md) · 呼出先 4件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a90.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004ab860 ["INT_ADD", "register:40f0:8", ["const:4ab860:8", "const:4:8"]]
+ 004ce6f8 ["INT_ADD", "register:40f0:8", ["const:4ce6f8:8", "const:4:8"]]
- 004ab874 ["INT_ADD", "register:40f0:8", ["const:4ab874:8", "const:4:8"]]
+ 004ce70c ["INT_ADD", "register:40f0:8", ["const:4ce70c:8", "const:4:8"]]
- 004ab890 ["INT_ADD", "register:40f0:8", ["const:4ab890:8", "const:4:8"]]
+ 004ce728 ["INT_ADD", "register:40f0:8", ["const:4ce728:8", "const:4:8"]]
~~~


### [`004abba0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004abba0.md) → [`004cea38`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004cea38.md) _ZN5Botan3MD510compress_nEPKhm

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb1b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57c00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004ac5b8 ["INT_ADD", "register:40f0:8", ["const:4ac5b8:8", "const:4:8"]]
+ 004cf450 ["INT_ADD", "register:40f0:8", ["const:4cf450:8", "const:4:8"]]
~~~


### [`004ac678`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac678.md) → [`004cf510`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf510.md) _ZN5Botan16MDx_HashFunction5clearEv

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb240`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57c90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004ac69c ["INT_ADD", "register:40f0:8", ["const:4ac69c:8", "const:4:8"]]
+ 004cf534 ["INT_ADD", "register:40f0:8", ["const:4cf534:8", "const:4:8"]]
~~~


### [`004ac704`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac704.md) → [`004cf59c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf59c.md) _ZN5Botan16MDx_HashFunction8add_dataEPKhm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb0f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57b40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004ac754 ["INT_ADD", "register:40f0:8", ["const:4ac754:8", "const:4:8"]]
+ 004cf5ec ["INT_ADD", "register:40f0:8", ["const:4cf5ec:8", "const:4:8"]]
- 004ac780 ["INT_ADD", "register:40f0:8", ["const:4ac780:8", "const:4:8"]]
+ 004cf618 ["INT_ADD", "register:40f0:8", ["const:4cf618:8", "const:4:8"]]
- 004ac7d4 ["INT_ADD", "register:40f0:8", ["const:4ac7d4:8", "const:4:8"]]
+ 004cf66c ["INT_ADD", "register:40f0:8", ["const:4cf66c:8", "const:4:8"]]
~~~


### [`004ac830`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac830.md) → [`004cf6c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf6c8.md) _ZN5Botan16MDx_HashFunction12final_resultEPh

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb240`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57c90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004ac8bc ["INT_ADD", "register:40f0:8", ["const:4ac8bc:8", "const:4:8"]]
+ 004cf754 ["INT_ADD", "register:40f0:8", ["const:4cf754:8", "const:4:8"]]
- 004ac8d0 ["INT_ADD", "register:40f0:8", ["const:4ac8d0:8", "const:4:8"]]
+ 004cf768 ["INT_ADD", "register:40f0:8", ["const:4cf768:8", "const:4:8"]]
- 004ac8ec ["INT_ADD", "register:40f0:8", ["const:4ac8ec:8", "const:4:8"]]
+ 004cf784 ["INT_ADD", "register:40f0:8", ["const:4cf784:8", "const:4:8"]]
~~~


### [`004acef0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004acef0.md) → [`004cfd88`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cfd88.md) _ZNK5Botan13PKCS7_Padding11add_paddingERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEmm

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00521e04`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521e04.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00544c9c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544c9c.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004acf5c ["INT_ADD", "register:40f0:8", ["const:4acf5c:8", "const:4:8"]]
+ 004cfdf4 ["INT_ADD", "register:40f0:8", ["const:4cfdf4:8", "const:4:8"]]
- 004acf88 ["INT_ADD", "register:40f0:8", ["const:4acf88:8", "const:4:8"]]
+ 004cfe20 ["INT_ADD", "register:40f0:8", ["const:4cfe20:8", "const:4:8"]]
~~~


### [`004ad3b4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ad3b4.md) → [`004d024c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d024c.md) _ZNK5Botan17ANSI_X923_Padding11add_paddingERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEmm

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0051e2cc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e2cc.md) [`00521e04`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521e04.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00541164`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541164.md) [`00544c9c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544c9c.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004ad404 ["INT_ADD", "register:40f0:8", ["const:4ad404:8", "const:4:8"]]
+ 004d029c ["INT_ADD", "register:40f0:8", ["const:4d029c:8", "const:4:8"]]
- 004ad450 ["INT_ADD", "register:40f0:8", ["const:4ad450:8", "const:4:8"]]
+ 004d02e8 ["INT_ADD", "register:40f0:8", ["const:4d02e8:8", "const:4:8"]]
- 004ad47c ["INT_ADD", "register:40f0:8", ["const:4ad47c:8", "const:4:8"]]
+ 004d0314 ["INT_ADD", "register:40f0:8", ["const:4d0314:8", "const:4:8"]]
~~~


### [`004ad87c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ad87c.md) → [`004d0714`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0714.md) _ZNK5Botan19OneAndZeros_Padding11add_paddingERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEmm

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051e2cc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e2cc.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00541164`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541164.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004ad8cc ["INT_ADD", "register:40f0:8", ["const:4ad8cc:8", "const:4:8"]]
+ 004d0764 ["INT_ADD", "register:40f0:8", ["const:4d0764:8", "const:4:8"]]
- 004ad920 ["INT_ADD", "register:40f0:8", ["const:4ad920:8", "const:4:8"]]
+ 004d07b8 ["INT_ADD", "register:40f0:8", ["const:4d07b8:8", "const:4:8"]]
- 004ad94c ["INT_ADD", "register:40f0:8", ["const:4ad94c:8", "const:4:8"]]
+ 004d07e4 ["INT_ADD", "register:40f0:8", ["const:4d07e4:8", "const:4:8"]]
~~~


### [`004ad9f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ad9f4.md) → [`004d088c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d088c.md) _ZNK5Botan11ESP_Padding11add_paddingERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEmm

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051e2cc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e2cc.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00541164`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541164.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004ada34 ["INT_ADD", "register:40f0:8", ["const:4ada34:8", "const:4:8"]]
+ 004d08cc ["INT_ADD", "register:40f0:8", ["const:4d08cc:8", "const:4:8"]]
- 004ada84 ["INT_ADD", "register:40f0:8", ["const:4ada84:8", "const:4:8"]]
+ 004d091c ["INT_ADD", "register:40f0:8", ["const:4d091c:8", "const:4:8"]]
~~~


### [`004ade98`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ade98.md) → [`004d0d30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0d30.md) _ZN5Botan12StreamCipher6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdc010`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc010.md) · 呼出先 4件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdbef0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbef0.md)
- 新版 呼出元 1件 [`00c58a60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a60.md) · 呼出先 4件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58940`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58940.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004adee0 ["INT_ADD", "register:40f0:8", ["const:4adee0:8", "const:4:8"]]
+ 004d0d78 ["INT_ADD", "register:40f0:8", ["const:4d0d78:8", "const:4:8"]]
- 004adeec ["INT_ADD", "register:40f0:8", ["const:4adeec:8", "const:4:8"]]
+ 004d0d84 ["INT_ADD", "register:40f0:8", ["const:4d0d84:8", "const:4:8"]]
- 004adefc ["INT_ADD", "register:40f0:8", ["const:4adefc:8", "const:4:8"]]
+ 004d0d94 ["INT_ADD", "register:40f0:8", ["const:4d0d94:8", "const:4:8"]]
~~~


### [`004aed68`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ae/004aed68.md) → [`004d1c00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d1/004d1c00.md) _ZN5Botan11Cipher_Mode9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00450668`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`0051dea4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dea4.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00473500`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`00540d3c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004aede0 ["INT_ADD", "register:40f0:8", ["const:4aede0:8", "const:4:8"]]
+ 004d1c78 ["INT_ADD", "register:40f0:8", ["const:4d1c78:8", "const:4:8"]]
- 004aedf0 ["INT_ADD", "register:40f0:8", ["const:4aedf0:8", "const:4:8"]]
+ 004d1c88 ["INT_ADD", "register:40f0:8", ["const:4d1c88:8", "const:4:8"]]
- 004aee00 ["INT_ADD", "register:40f0:8", ["const:4aee00:8", "const:4:8"]]
+ 004d1c98 ["INT_ADD", "register:40f0:8", ["const:4d1c98:8", "const:4:8"]]
~~~


### [`004b3f90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3f90.md) → [`004d6e28`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6e28.md) FUN_004d6e28

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00494d38`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494d38.md) [`0049731c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/0049731c.md) [`004b87c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b87c8.md) [`004bc804`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bc804.md) [`004bd550`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bd550.md) · 呼出先 10件 [`00496208`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496208.md) [`004af0b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004af/004af0b8.md) [`004af4c4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004af/004af4c4.md) [`004afcb8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004af/004afcb8.md) [`004b088c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b0/004b088c.md)
- 新版 呼出元 5件 [`004b7bd0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7bd0.md) [`004ba1b4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba1b4.md) [`004db660`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db660.md) [`004df69c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df69c.md) [`004e03e8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e03e8.md) · 呼出先 10件 [`004b90a0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b90a0.md) [`004d1f50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d1/004d1f50.md) [`004d235c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d2/004d235c.md) [`004d2b50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d2/004d2b50.md) [`004d3724`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d3/004d3724.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004b3fdc ["INT_ADD", "register:40f0:8", ["const:4b3fdc:8", "const:4:8"]]
+ 004d6e74 ["INT_ADD", "register:40f0:8", ["const:4d6e74:8", "const:4:8"]]
- 004b41d4 ["INT_ADD", "register:40f0:8", ["const:4b41d4:8", "const:4:8"]]
+ 004d706c ["INT_ADD", "register:40f0:8", ["const:4d706c:8", "const:4:8"]]
~~~


### [`004b423c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b423c.md) → [`004d70d4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d70d4.md) FUN_004d70d4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`004b3f90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3f90.md) [`004b44b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b44b8.md) [`004b47ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b47ec.md) [`004b4a30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b4a30.md) · 呼出先 1件 [`00bdb240`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 4件 [`004d6e28`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6e28.md) [`004d7350`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7350.md) [`004d7684`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7684.md) [`004d78c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d78c8.md) · 呼出先 1件 [`00c57c90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004b4278 ["INT_ADD", "register:40f0:8", ["const:4b4278:8", "const:4:8"]]
+ 004d7110 ["INT_ADD", "register:40f0:8", ["const:4d7110:8", "const:4:8"]]
~~~


### [`004b44b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b44b8.md) → [`004d7350`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7350.md) FUN_004d7350

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004b3f90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3f90.md) [`004b44b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b44b8.md) · 呼出先 11件 [`004958dc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004958dc.md) [`00495a74`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495a74.md) [`00495c94`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495c94.md) [`004af4c4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004af/004af4c4.md) [`004afcb8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004af/004afcb8.md)
- 新版 呼出元 2件 [`004d6e28`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6e28.md) [`004d7350`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7350.md) · 呼出先 11件 [`004b8774`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8774.md) [`004b890c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b890c.md) [`004b8b2c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8b2c.md) [`004d235c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d2/004d235c.md) [`004d2b50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d2/004d2b50.md)

変更の種類 constant, operands_and_dependencies

~~~diff
- 004b4510 ["INT_ADD", "register:40f0:8", ["const:4b4510:8", "const:4:8"]]
+ 004d73a8 ["INT_ADD", "register:40f0:8", ["const:4d73a8:8", "const:4:8"]]
- 004b4528 ["INT_ADD", "register:40f0:8", ["const:4b4528:8", "const:4:8"]]
+ 004d73c0 ["INT_ADD", "register:40f0:8", ["const:4d73c0:8", "const:4:8"]]
- 004b4540 ["INT_ADD", "register:40f0:8", ["const:4b4540:8", "const:4:8"]]
+ 004d73d8 ["INT_ADD", "register:40f0:8", ["const:4d73d8:8", "const:4:8"]]
~~~


