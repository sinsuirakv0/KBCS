# 00affb3c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0170.md#review-4a97de270e400e48432b94b95875a028)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afff64`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aff/00afff64.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0066.md#compare-24cf9f49b97e57df4806f535e27eb184)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00affb3c",
  "name": "FUN_00affb3c",
  "size": 240,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4036a8623f168a20d2ccd884287421a810fa5ae01058952c06ecdfce7e4bc657",
  "source_text_sha256": "4036a8623f168a20d2ccd884287421a810fa5ae01058952c06ecdfce7e4bc657",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00affb3c",
        "00affc2b"
      ]
    ],
    "bytes_sha256": "e10f4dd338e3481f11cc97d7101ecd5f7a7685fe6fe22146a5ba9033ab760551",
    "instruction_count": 60,
    "instruction_bytes": 240,
    "body_bytes": 240,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0098c828](../0098c/0098c828.md)
- [00affc2c](../00aff/00affc2c.md)

## 呼び出し先

- [0046da7c](../0046d/0046da7c.md)
- [005e73e0](../005e7/005e73e0.md)
- [008514b8](../00851/008514b8.md)
- [00afe6c0](../00afe/00afe6c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 711 bytes

~~~c

int FUN_00affb3c(int param_1,int param_2,int param_3)

{
  int iVar1;
  int iVar2;
  long lVar3;
  ulong uVar4;
  
  lVar3 = FUN_008514b8();
  uVar4 = FUN_005e73e0(lVar3 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar4 & 1) == 0) {
    iVar2 = 0;
  }
  else {
    lVar3 = FUN_008514b8();
    iVar2 = *(int *)(lVar3 + (long)param_2 * 0x770 + (long)param_3 * 0x1dc + 0xa05c8);
    iVar1 = FUN_00afe6c0(param_1,param_2,param_3,0x19,0);
                    /* catch() { ... } // from try @ 00aff548 with catch @ 00affbc0 */
    iVar2 = FUN_0046da7c(iVar2 + iVar1 * -100,0);
    iVar1 = FUN_00afe6c0(param_1,param_2,param_3,0x3f4,0);
    iVar2 = (((100 - iVar1) * (iVar2 / 100)) / 100) * 100;
  }
  return iVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00affb3c"></a> `00affb3c` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00affb40"></a> `00affb40` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00affb44"></a> `00affb44` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00affb48"></a> `00affb48` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00affb4c"></a> `00affb4c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00affb50"></a> `00affb50` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00affb54"></a> `00affb54` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00affb58"></a> `00affb58` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00affb5c"></a> `00affb5c` | `57 46 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00affb60"></a> `00affb60` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00affb64"></a> `00affb64` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00affb68"></a> `00affb68` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00affb6c"></a> `00affb6c` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00affb70"></a> `00affb70` | `1c 9e eb 97` | bl 0x005e73e0 | `UNCONDITIONAL_CALL`
<a id="insn-00affb74"></a> `00affb74` | `60 00 00 37` | tbnz w0,#0x0,0x00affb80 | `CONDITIONAL_JUMP`
<a id="insn-00affb78"></a> `00affb78` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00affb7c"></a> `00affb7c` | `27 00 00 14` | b 0x00affc18 | `UNCONDITIONAL_JUMP`
<a id="insn-00affb80"></a> `00affb80` | `4e 46 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00affb84"></a> `00affb84` | `08 ee 80 52` | mov w8,#0x770 | `FALL_THROUGH`
<a id="insn-00affb88"></a> `00affb88` | `89 3b 80 52` | mov w9,#0x1dc | `FALL_THROUGH`
<a id="insn-00affb8c"></a> `00affb8c` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00affb90"></a> `00affb90` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00affb94"></a> `00affb94` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00affb98"></a> `00affb98` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00affb9c"></a> `00affb9c` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00affba0"></a> `00affba0` | `09 b9 80 52` | mov w9,#0x5c8 | `FALL_THROUGH`
<a id="insn-00affba4"></a> `00affba4` | `23 03 80 52` | mov w3,#0x19 | `FALL_THROUGH`
<a id="insn-00affba8"></a> `00affba8` | `49 01 a0 72` | movk w9,#0xa, LSL #16 | `FALL_THROUGH`
<a id="insn-00affbac"></a> `00affbac` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00affbb0"></a> `00affbb0` | `16 69 69 b8` | ldr w22,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00affbb4"></a> `00affbb4` | `c3 fa ff 97` | bl 0x00afe6c0 | `UNCONDITIONAL_CALL`
<a id="insn-00affbb8"></a> `00affbb8` | `68 0c 80 12` | mov w8,#0xffffff9c | `FALL_THROUGH`
<a id="insn-00affbbc"></a> `00affbbc` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00affbc0"></a> `00affbc0` | `00 58 08 1b` | madd w0,w0,w8,w22 | `FALL_THROUGH`
<a id="insn-00affbc4"></a> `00affbc4` | `ae b7 e5 97` | bl 0x0046da7c | `UNCONDITIONAL_CALL`
<a id="insn-00affbc8"></a> `00affbc8` | `f6 a3 90 52` | mov w22,#0x851f | `FALL_THROUGH`
<a id="insn-00affbcc"></a> `00affbcc` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00affbd0"></a> `00affbd0` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00affbd4"></a> `00affbd4` | `76 3d aa 72` | movk w22,#0x51eb, LSL #16 | `FALL_THROUGH`
<a id="insn-00affbd8"></a> `00affbd8` | `83 7e 80 52` | mov w3,#0x3f4 | `FALL_THROUGH`
<a id="insn-00affbdc"></a> `00affbdc` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00affbe0"></a> `00affbe0` | `08 7c 36 9b` | smull x8,w0,w22 | `FALL_THROUGH`
<a id="insn-00affbe4"></a> `00affbe4` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00affbe8"></a> `00affbe8` | `09 fd 7f d3` | lsr x9,x8,#0x3f | `FALL_THROUGH`
<a id="insn-00affbec"></a> `00affbec` | `08 fd 65 93` | asr x8,x8,#0x25 | `FALL_THROUGH`
<a id="insn-00affbf0"></a> `00affbf0` | `17 01 09 0b` | add w23,w8,w9 | `FALL_THROUGH`
<a id="insn-00affbf4"></a> `00affbf4` | `b3 fa ff 97` | bl 0x00afe6c0 | `UNCONDITIONAL_CALL`
<a id="insn-00affbf8"></a> `00affbf8` | `88 0c 80 52` | mov w8,#0x64 | `FALL_THROUGH`
<a id="insn-00affbfc"></a> `00affbfc` | `09 01 00 4b` | sub w9,w8,w0 | `FALL_THROUGH`
<a id="insn-00affc00"></a> `00affc00` | `29 7d 17 1b` | mul w9,w9,w23 | `FALL_THROUGH`
<a id="insn-00affc04"></a> `00affc04` | `29 7d 36 9b` | smull x9,w9,w22 | `FALL_THROUGH`
<a id="insn-00affc08"></a> `00affc08` | `2a fd 7f d3` | lsr x10,x9,#0x3f | `FALL_THROUGH`
<a id="insn-00affc0c"></a> `00affc0c` | `29 fd 65 93` | asr x9,x9,#0x25 | `FALL_THROUGH`
<a id="insn-00affc10"></a> `00affc10` | `29 01 0a 0b` | add w9,w9,w10 | `FALL_THROUGH`
<a id="insn-00affc14"></a> `00affc14` | `20 7d 08 1b` | mul w0,w9,w8 | `FALL_THROUGH`
<a id="insn-00affc18"></a> `00affc18` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00affc1c"></a> `00affc1c` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00affc20"></a> `00affc20` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00affc24"></a> `00affc24` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00affc28"></a> `00affc28` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00affb3c`](#insn-00affb3c) 範囲 `[['00affb3c', '00affb77']]`
  - `CONDITIONAL_JUMP` [`00affb74`](#insn-00affb74) → [`00affb80`](#insn-00affb80)
  - `FALL_THROUGH` [`00affb74`](#insn-00affb74) → [`00affb78`](#insn-00affb78)
- ブロック [`00affb78`](#insn-00affb78) 範囲 `[['00affb78', '00affb7f']]`
  - `UNCONDITIONAL_JUMP` [`00affb7c`](#insn-00affb7c) → [`00affc18`](#insn-00affc18)
- ブロック [`00affb80`](#insn-00affb80) 範囲 `[['00affb80', '00affbbf']]`
  - `FALL_THROUGH` [`00affbbc`](#insn-00affbbc) → [`00affbc0`](#insn-00affbc0)
- ブロック [`00affbc0`](#insn-00affbc0) 範囲 `[['00affbc0', '00affc17']]`
  - `FALL_THROUGH` [`00affc14`](#insn-00affc14) → [`00affc18`](#insn-00affc18)
- ブロック [`00affc18`](#insn-00affc18) 範囲 `[['00affc18', '00affc2b']]`

## 命令位置別の参照

- [`00affb3c`](#insn-00affb3c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb40`](#insn-00affb40) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb44`](#insn-00affb44) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb48`](#insn-00affb48) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb5c`](#insn-00affb5c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00affb70`](#insn-00affb70) → [`005e73e0`](../005e7/005e73e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e73e0` · 推定シンボル `None` · 推定型 `None`
- [`00affb74`](#insn-00affb74) → [`00affb80`](#insn-00affb80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb7c`](#insn-00affb7c) → [`00affc18`](#insn-00affc18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb80`](#insn-00affb80) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00affbb4`](#insn-00affbb4) → [`00afe6c0`](../00afe/00afe6c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00afe6c0` · 推定シンボル `None` · 推定型 `None`
- [`00affbc4`](#insn-00affbc4) → [`0046da7c`](../0046d/0046da7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046da7c` · 推定シンボル `None` · 推定型 `None`
- [`00affbf4`](#insn-00affbf4) → [`00afe6c0`](../00afe/00afe6c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00afe6c0` · 推定シンボル `None` · 推定型 `None`
- [`00affc18`](#insn-00affc18) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc1c`](#insn-00affc1c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc20`](#insn-00affc20) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc24`](#insn-00affc24) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00affb3c`](#insn-00affb3c)

~~~json
{
  "source": "00affb3c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb40`](#insn-00affb40)

~~~json
{
  "source": "00affb40",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb44`](#insn-00affb44)

~~~json
{
  "source": "00affb44",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb48`](#insn-00affb48)

~~~json
{
  "source": "00affb48",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb5c`](#insn-00affb5c)

~~~json
{
  "source": "00affb5c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affb70`](#insn-00affb70)

~~~json
{
  "source": "00affb70",
  "target": "005e73e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affb74`](#insn-00affb74)

~~~json
{
  "source": "00affb74",
  "target": "00affb80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb7c`](#insn-00affb7c)

~~~json
{
  "source": "00affb7c",
  "target": "00affc18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb80`](#insn-00affb80)

~~~json
{
  "source": "00affb80",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affbb4`](#insn-00affbb4)

~~~json
{
  "source": "00affbb4",
  "target": "00afe6c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affbc4`](#insn-00affbc4)

~~~json
{
  "source": "00affbc4",
  "target": "0046da7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affbf4`](#insn-00affbf4)

~~~json
{
  "source": "00affbf4",
  "target": "00afe6c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affc18`](#insn-00affc18)

~~~json
{
  "source": "00affc18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc1c`](#insn-00affc1c)

~~~json
{
  "source": "00affc1c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc20`](#insn-00affc20)

~~~json
{
  "source": "00affc20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc24`](#insn-00affc24)

~~~json
{
  "source": "00affc24",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
