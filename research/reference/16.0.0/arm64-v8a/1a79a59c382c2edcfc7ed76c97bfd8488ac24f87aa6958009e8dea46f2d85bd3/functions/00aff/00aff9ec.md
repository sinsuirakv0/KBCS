# 00aff9ec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0170.md#review-d19eea21fdd9fd5b1705a53195a83aa3)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00affe14`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aff/00affe14.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0066.md#compare-e14431371b80498e98feda9357a1a2f9)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aff9ec",
  "name": "FUN_00aff9ec",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e99e491ae8a8c1d1b931a9889376936d86cb948746340a3d5c9f7ebbb69586f3",
  "source_text_sha256": "e99e491ae8a8c1d1b931a9889376936d86cb948746340a3d5c9f7ebbb69586f3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aff9ec",
        "00affab3"
      ]
    ],
    "bytes_sha256": "0c83b01c196e0856e3b9748617acf02f8ebebdb0b2256d3c2c24d0fb9ab508df",
    "instruction_count": 50,
    "instruction_bytes": 200,
    "body_bytes": 200,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a4f1bc](../00a4f/00a4f1bc.md)

## 呼び出し先

- [005e73e0](../005e7/005e73e0.md)
- [008514b8](../00851/008514b8.md)
- [00afe6c0](../00afe/00afe6c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1446 bytes

~~~c

int FUN_00aff9ec(int param_1,int param_2,int param_3)

{
  int iVar1;
  int iVar2;
  long lVar3;
  ulong uVar4;
  
                    /* catch() { ... } // from try @ 00aff874 with catch @ 00affa04 */
                    /* catch() { ... } // from try @ 00aff7ec with catch @ 00affa08 */
  lVar3 = FUN_008514b8();
                    /* catch() { ... } // from try @ 00aff820 with catch @ 00affa10 */
                    /* catch() { ... } // from try @ 00aff62c with catch @ 00affa18 */
                    /* catch() { ... } // from try @ 00aff5d8 with catch @ 00affa1c */
  uVar4 = FUN_005e73e0(lVar3 + (long)param_1 * 0x1f0 + 0x2768);
  lVar3 = FUN_008514b8();
  if ((uVar4 & 1) == 0) {
                    /* catch() { ... } // from try @ 00aff5cc with catch @ 00affa34 */
    iVar1 = *(int *)((long)__DT_JMPREL + lVar3 + ((long)param_2 + 2) * 0x1c4 + 0x1808);
                    /* catch() { ... } // from try @ 00aff594 with catch @ 00affa48 */
  }
  else {
                    /* catch() { ... } // from try @ 00aff4e4 with catch @ 00affa4c */
                    /* catch() { ... } // from try @ 00aff4d0 with catch @ 00affa60 */
    iVar1 = *(int *)(lVar3 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9f6e0);
    iVar2 = FUN_00afe6c0(param_1,param_2,param_3,0x3d,0);
                    /* catch() { ... } // from try @ 00aff47c with catch @ 00affa8c */
    iVar1 = ((100 - iVar2) * iVar1) / 100;
  }
  return iVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aff9ec"></a> `00aff9ec` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aff9f0"></a> `00aff9f0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aff9f4"></a> `00aff9f4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aff9f8"></a> `00aff9f8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aff9fc"></a> `00aff9fc` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00affa00"></a> `00affa00` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00affa04"></a> `00affa04` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00affa08"></a> `00affa08` | `ac 46 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00affa0c"></a> `00affa0c` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00affa10"></a> `00affa10` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00affa14"></a> `00affa14` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00affa18"></a> `00affa18` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00affa1c"></a> `00affa1c` | `71 9e eb 97` | bl 0x005e73e0 | `UNCONDITIONAL_CALL`
<a id="insn-00affa20"></a> `00affa20` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00affa24"></a> `00affa24` | `a5 46 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00affa28"></a> `00affa28` | `88 7e 40 93` | sxtw x8,w20 | `FALL_THROUGH`
<a id="insn-00affa2c"></a> `00affa2c` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00affa30"></a> `00affa30` | `f6 00 00 37` | tbnz w22,#0x0,0x00affa4c | `CONDITIONAL_JUMP`
<a id="insn-00affa34"></a> `00affa34` | `89 38 80 52` | mov w9,#0x1c4 | `FALL_THROUGH`
<a id="insn-00affa38"></a> `00affa38` | `08 01 09 9b` | madd x8,x8,x9,x0 | `FALL_THROUGH`
<a id="insn-00affa3c"></a> `00affa3c` | `09 54 9a 52` | mov w9,#0xd2a0 | `FALL_THROUGH`
<a id="insn-00affa40"></a> `00affa40` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00affa44"></a> `00affa44` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00affa48"></a> `00affa48` | `17 00 00 14` | b 0x00affaa4 | `UNCONDITIONAL_JUMP`
<a id="insn-00affa4c"></a> `00affa4c` | `09 ee 80 52` | mov w9,#0x770 | `FALL_THROUGH`
<a id="insn-00affa50"></a> `00affa50` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00affa54"></a> `00affa54` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00affa58"></a> `00affa58` | `08 01 09 9b` | madd x8,x8,x9,x0 | `FALL_THROUGH`
<a id="insn-00affa5c"></a> `00affa5c` | `89 3b 80 52` | mov w9,#0x1dc | `FALL_THROUGH`
<a id="insn-00affa60"></a> `00affa60` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00affa64"></a> `00affa64` | `a3 07 80 52` | mov w3,#0x3d | `FALL_THROUGH`
<a id="insn-00affa68"></a> `00affa68` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00affa6c"></a> `00affa6c` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00affa70"></a> `00affa70` | `09 dc 9e 52` | mov w9,#0xf6e0 | `FALL_THROUGH`
<a id="insn-00affa74"></a> `00affa74` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00affa78"></a> `00affa78` | `16 69 69 b8` | ldr w22,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00affa7c"></a> `00affa7c` | `11 fb ff 97` | bl 0x00afe6c0 | `UNCONDITIONAL_CALL`
<a id="insn-00affa80"></a> `00affa80` | `88 0c 80 52` | mov w8,#0x64 | `FALL_THROUGH`
<a id="insn-00affa84"></a> `00affa84` | `e9 a3 90 52` | mov w9,#0x851f | `FALL_THROUGH`
<a id="insn-00affa88"></a> `00affa88` | `08 01 00 4b` | sub w8,w8,w0 | `FALL_THROUGH`
<a id="insn-00affa8c"></a> `00affa8c` | `69 3d aa 72` | movk w9,#0x51eb, LSL #16 | `FALL_THROUGH`
<a id="insn-00affa90"></a> `00affa90` | `08 7d 16 1b` | mul w8,w8,w22 | `FALL_THROUGH`
<a id="insn-00affa94"></a> `00affa94` | `08 7d 29 9b` | smull x8,w8,w9 | `FALL_THROUGH`
<a id="insn-00affa98"></a> `00affa98` | `09 fd 7f d3` | lsr x9,x8,#0x3f | `FALL_THROUGH`
<a id="insn-00affa9c"></a> `00affa9c` | `08 fd 65 93` | asr x8,x8,#0x25 | `FALL_THROUGH`
<a id="insn-00affaa0"></a> `00affaa0` | `00 01 09 0b` | add w0,w8,w9 | `FALL_THROUGH`
<a id="insn-00affaa4"></a> `00affaa4` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00affaa8"></a> `00affaa8` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00affaac"></a> `00affaac` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00affab0"></a> `00affab0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aff9ec`](#insn-00aff9ec) 範囲 `[['00aff9ec', '00affa03']]`
  - `FALL_THROUGH` [`00affa00`](#insn-00affa00) → [`00affa04`](#insn-00affa04)
- ブロック [`00affa04`](#insn-00affa04) 範囲 `[['00affa04', '00affa07']]`
  - `FALL_THROUGH` [`00affa04`](#insn-00affa04) → [`00affa08`](#insn-00affa08)
- ブロック [`00affa08`](#insn-00affa08) 範囲 `[['00affa08', '00affa0f']]`
  - `FALL_THROUGH` [`00affa0c`](#insn-00affa0c) → [`00affa10`](#insn-00affa10)
- ブロック [`00affa10`](#insn-00affa10) 範囲 `[['00affa10', '00affa17']]`
  - `FALL_THROUGH` [`00affa14`](#insn-00affa14) → [`00affa18`](#insn-00affa18)
- ブロック [`00affa18`](#insn-00affa18) 範囲 `[['00affa18', '00affa1b']]`
  - `FALL_THROUGH` [`00affa18`](#insn-00affa18) → [`00affa1c`](#insn-00affa1c)
- ブロック [`00affa1c`](#insn-00affa1c) 範囲 `[['00affa1c', '00affa33']]`
  - `CONDITIONAL_JUMP` [`00affa30`](#insn-00affa30) → [`00affa4c`](#insn-00affa4c)
  - `FALL_THROUGH` [`00affa30`](#insn-00affa30) → [`00affa34`](#insn-00affa34)
- ブロック [`00affa34`](#insn-00affa34) 範囲 `[['00affa34', '00affa47']]`
  - `FALL_THROUGH` [`00affa44`](#insn-00affa44) → [`00affa48`](#insn-00affa48)
- ブロック [`00affa48`](#insn-00affa48) 範囲 `[['00affa48', '00affa4b']]`
  - `UNCONDITIONAL_JUMP` [`00affa48`](#insn-00affa48) → [`00affaa4`](#insn-00affaa4)
- ブロック [`00affa4c`](#insn-00affa4c) 範囲 `[['00affa4c', '00affa5f']]`
  - `FALL_THROUGH` [`00affa5c`](#insn-00affa5c) → [`00affa60`](#insn-00affa60)
- ブロック [`00affa60`](#insn-00affa60) 範囲 `[['00affa60', '00affa8b']]`
  - `FALL_THROUGH` [`00affa88`](#insn-00affa88) → [`00affa8c`](#insn-00affa8c)
- ブロック [`00affa8c`](#insn-00affa8c) 範囲 `[['00affa8c', '00affaa3']]`
  - `FALL_THROUGH` [`00affaa0`](#insn-00affaa0) → [`00affaa4`](#insn-00affaa4)
- ブロック [`00affaa4`](#insn-00affaa4) 範囲 `[['00affaa4', '00affab3']]`

## 命令位置別の参照

- [`00aff9ec`](#insn-00aff9ec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff9f0`](#insn-00aff9f0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff9f4`](#insn-00aff9f4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affa08`](#insn-00affa08) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00affa1c`](#insn-00affa1c) → [`005e73e0`](../005e7/005e73e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e73e0` · 推定シンボル `None` · 推定型 `None`
- [`00affa24`](#insn-00affa24) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00affa30`](#insn-00affa30) → [`00affa4c`](#insn-00affa4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affa44`](#insn-00affa44) → `0023d2a0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00affa48`](#insn-00affa48) → [`00affaa4`](#insn-00affaa4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affa7c`](#insn-00affa7c) → [`00afe6c0`](../00afe/00afe6c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00afe6c0` · 推定シンボル `None` · 推定型 `None`
- [`00affaa4`](#insn-00affaa4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affaa8`](#insn-00affaa8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affaac`](#insn-00affaac) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aff9ec`](#insn-00aff9ec)

~~~json
{
  "source": "00aff9ec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff9f0`](#insn-00aff9f0)

~~~json
{
  "source": "00aff9f0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff9f4`](#insn-00aff9f4)

~~~json
{
  "source": "00aff9f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affa08`](#insn-00affa08)

~~~json
{
  "source": "00affa08",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affa1c`](#insn-00affa1c)

~~~json
{
  "source": "00affa1c",
  "target": "005e73e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affa24`](#insn-00affa24)

~~~json
{
  "source": "00affa24",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affa30`](#insn-00affa30)

~~~json
{
  "source": "00affa30",
  "target": "00affa4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affa44`](#insn-00affa44)

~~~json
{
  "source": "00affa44",
  "target": "0023d2a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6152,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0bab9000000000002040000010000000000000000000000d8bab90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00affa48`](#insn-00affa48)

~~~json
{
  "source": "00affa48",
  "target": "00affaa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affa7c`](#insn-00affa7c)

~~~json
{
  "source": "00affa7c",
  "target": "00afe6c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affaa4`](#insn-00affaa4)

~~~json
{
  "source": "00affaa4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affaa8`](#insn-00affaa8)

~~~json
{
  "source": "00affaa8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affaac`](#insn-00affaac)

~~~json
{
  "source": "00affaac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
