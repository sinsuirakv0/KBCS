# 00bf1bac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b75164`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75164.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0019.md#compare-09d8fc89fe3784c311c7f0340b8dd614)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bf1fd4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1fd4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0040.md#compare-bf12d058324b2ff54b2d9297f1ebd484)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf1bac",
  "name": "_ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEPKcmm",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "acd845f5b67359a24cecad3f0f8a76c227148df935f0170de9b8b2a2809c18de",
  "source_text_sha256": "acd845f5b67359a24cecad3f0f8a76c227148df935f0170de9b8b2a2809c18de",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf1bac",
        "00bf1c7b"
      ]
    ],
    "bytes_sha256": "ab47e64287983482a64433a83c653c3d62a97609f9e7662c20b8efb43e528e68",
    "instruction_count": 52,
    "instruction_bytes": 208,
    "body_bytes": 208,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57bd0](../00c57/00c57bd0.md)
- [00c57c50](../00c57/00c57c50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1288 bytes

~~~c

ulong _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEPKcmm
                (byte *param_1,byte *param_2,ulong param_3,size_t param_4)

{
  byte *pbVar1;
  ulong uVar2;
  byte *pbVar3;
  byte bVar4;
  int iVar5;
  byte *pbVar6;
  long lVar7;
  byte *pbVar8;
  
  uVar2 = *(ulong *)(param_1 + 8);
  pbVar3 = *(byte **)(param_1 + 0x10);
  if ((*param_1 & 1) == 0) {
    pbVar3 = param_1 + 1;
    uVar2 = (ulong)(*param_1 >> 1);
  }
  if (uVar2 < param_3) {
    param_3 = 0xffffffffffffffff;
  }
  else if (param_4 != 0) {
    pbVar6 = pbVar3 + param_3;
    pbVar1 = pbVar3 + uVar2;
    lVar7 = (long)pbVar1 - (long)pbVar6;
    pbVar8 = pbVar1;
    if ((long)param_4 <= lVar7) {
      bVar4 = *param_2;
      do {
        pbVar8 = pbVar1;
        if (((0xfffffffffffffffe < lVar7 - param_4) ||
            (pbVar6 = memchr(pbVar6,(uint)bVar4,(lVar7 - param_4) + 1), pbVar6 == (byte *)0x0)) ||
           (iVar5 = memcmp(pbVar6,param_2,param_4), pbVar8 = pbVar6, iVar5 == 0)) break;
        pbVar6 = pbVar6 + 1;
        lVar7 = (long)pbVar1 - (long)pbVar6;
        pbVar8 = pbVar1;
      } while ((long)param_4 <= lVar7);
    }
    param_3 = (long)pbVar8 - (long)pbVar3;
    if (pbVar8 == pbVar1) {
      param_3 = 0xffffffffffffffff;
    }
  }
  return param_3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf1bac"></a> `00bf1bac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bf1bb0"></a> `00bf1bb0` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bf1bb4"></a> `00bf1bb4` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf1bb8"></a> `00bf1bb8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bf1bbc"></a> `00bf1bbc` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bf1bc0"></a> `00bf1bc0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bf1bc4"></a> `00bf1bc4` | `08 00 40 39` | ldrb w8,[x0] | `FALL_THROUGH`
<a id="insn-00bf1bc8"></a> `00bf1bc8` | `09 ac 40 a9` | ldp x9,x11,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bf1bcc"></a> `00bf1bcc` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf1bd0"></a> `00bf1bd0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf1bd4"></a> `00bf1bd4` | `77 15 80 9a` | csinc x23,x11,x0,ne | `FALL_THROUGH`
<a id="insn-00bf1bd8"></a> `00bf1bd8` | `48 01 89 9a` | csel x8,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bf1bdc"></a> `00bf1bdc` | `1f 01 02 eb` | cmp x8,x2 | `FALL_THROUGH`
<a id="insn-00bf1be0"></a> `00bf1be0` | `62 00 00 54` | b.cs 0x00bf1bec | `CONDITIONAL_JUMP`
<a id="insn-00bf1be4"></a> `00bf1be4` | `02 00 80 92` | mov x2,#-0x1 | `FALL_THROUGH`
<a id="insn-00bf1be8"></a> `00bf1be8` | `0c 00 00 14` | b 0x00bf1c18 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf1bec"></a> `00bf1bec` | `f3 03 03 aa` | mov x19,x3 | `FALL_THROUGH`
<a id="insn-00bf1bf0"></a> `00bf1bf0` | `43 01 00 b4` | cbz x3,0x00bf1c18 | `CONDITIONAL_JUMP`
<a id="insn-00bf1bf4"></a> `00bf1bf4` | `e0 02 02 8b` | add x0,x23,x2 | `FALL_THROUGH`
<a id="insn-00bf1bf8"></a> `00bf1bf8` | `f8 02 08 8b` | add x24,x23,x8 | `FALL_THROUGH`
<a id="insn-00bf1bfc"></a> `00bf1bfc` | `08 03 00 cb` | sub x8,x24,x0 | `FALL_THROUGH`
<a id="insn-00bf1c00"></a> `00bf1c00` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00bf1c04"></a> `00bf1c04` | `8a 01 00 54` | b.ge 0x00bf1c34 | `CONDITIONAL_JUMP`
<a id="insn-00bf1c08"></a> `00bf1c08` | `f6 03 18 aa` | mov x22,x24 | `FALL_THROUGH`
<a id="insn-00bf1c0c"></a> `00bf1c0c` | `c8 02 17 cb` | sub x8,x22,x23 | `FALL_THROUGH`
<a id="insn-00bf1c10"></a> `00bf1c10` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00bf1c14"></a> `00bf1c14` | `02 11 9f da` | csinv x2,x8,xzr,ne | `FALL_THROUGH`
<a id="insn-00bf1c18"></a> `00bf1c18` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bf1c1c"></a> `00bf1c1c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bf1c20"></a> `00bf1c20` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bf1c24"></a> `00bf1c24` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf1c28"></a> `00bf1c28` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bf1c2c"></a> `00bf1c2c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bf1c30"></a> `00bf1c30` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bf1c34"></a> `00bf1c34` | `35 00 40 39` | ldrb w21,[x1] | `FALL_THROUGH`
<a id="insn-00bf1c38"></a> `00bf1c38` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bf1c3c"></a> `00bf1c3c` | `08 01 13 cb` | sub x8,x8,x19 | `FALL_THROUGH`
<a id="insn-00bf1c40"></a> `00bf1c40` | `02 05 00 b1` | adds x2,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf1c44"></a> `00bf1c44` | `22 fe ff 54` | b.cs 0x00bf1c08 | `CONDITIONAL_JUMP`
<a id="insn-00bf1c48"></a> `00bf1c48` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00bf1c4c"></a> `00bf1c4c` | `e1 97 01 94` | bl 0x00c57bd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bf1c50"></a> `00bf1c50` | `c0 fd ff b4` | cbz x0,0x00bf1c08 | `CONDITIONAL_JUMP`
<a id="insn-00bf1c54"></a> `00bf1c54` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bf1c58"></a> `00bf1c58` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bf1c5c"></a> `00bf1c5c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bf1c60"></a> `00bf1c60` | `fc 97 01 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bf1c64"></a> `00bf1c64` | `40 fd ff 34` | cbz w0,0x00bf1c0c | `CONDITIONAL_JUMP`
<a id="insn-00bf1c68"></a> `00bf1c68` | `c0 06 00 91` | add x0,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00bf1c6c"></a> `00bf1c6c` | `08 03 00 cb` | sub x8,x24,x0 | `FALL_THROUGH`
<a id="insn-00bf1c70"></a> `00bf1c70` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00bf1c74"></a> `00bf1c74` | `4a fe ff 54` | b.ge 0x00bf1c3c | `CONDITIONAL_JUMP`
<a id="insn-00bf1c78"></a> `00bf1c78` | `e4 ff ff 17` | b 0x00bf1c08 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bf1bac`](#insn-00bf1bac) 範囲 `[['00bf1bac', '00bf1be3']]`
  - `CONDITIONAL_JUMP` [`00bf1be0`](#insn-00bf1be0) → [`00bf1bec`](#insn-00bf1bec)
  - `FALL_THROUGH` [`00bf1be0`](#insn-00bf1be0) → [`00bf1be4`](#insn-00bf1be4)
- ブロック [`00bf1be4`](#insn-00bf1be4) 範囲 `[['00bf1be4', '00bf1beb']]`
  - `UNCONDITIONAL_JUMP` [`00bf1be8`](#insn-00bf1be8) → [`00bf1c18`](#insn-00bf1c18)
- ブロック [`00bf1bec`](#insn-00bf1bec) 範囲 `[['00bf1bec', '00bf1bf3']]`
  - `CONDITIONAL_JUMP` [`00bf1bf0`](#insn-00bf1bf0) → [`00bf1c18`](#insn-00bf1c18)
  - `FALL_THROUGH` [`00bf1bf0`](#insn-00bf1bf0) → [`00bf1bf4`](#insn-00bf1bf4)
- ブロック [`00bf1bf4`](#insn-00bf1bf4) 範囲 `[['00bf1bf4', '00bf1c07']]`
  - `CONDITIONAL_JUMP` [`00bf1c04`](#insn-00bf1c04) → [`00bf1c34`](#insn-00bf1c34)
  - `FALL_THROUGH` [`00bf1c04`](#insn-00bf1c04) → [`00bf1c08`](#insn-00bf1c08)
- ブロック [`00bf1c08`](#insn-00bf1c08) 範囲 `[['00bf1c08', '00bf1c0b']]`
  - `FALL_THROUGH` [`00bf1c08`](#insn-00bf1c08) → [`00bf1c0c`](#insn-00bf1c0c)
- ブロック [`00bf1c0c`](#insn-00bf1c0c) 範囲 `[['00bf1c0c', '00bf1c17']]`
  - `FALL_THROUGH` [`00bf1c14`](#insn-00bf1c14) → [`00bf1c18`](#insn-00bf1c18)
- ブロック [`00bf1c18`](#insn-00bf1c18) 範囲 `[['00bf1c18', '00bf1c33']]`
- ブロック [`00bf1c34`](#insn-00bf1c34) 範囲 `[['00bf1c34', '00bf1c3b']]`
  - `FALL_THROUGH` [`00bf1c38`](#insn-00bf1c38) → [`00bf1c3c`](#insn-00bf1c3c)
- ブロック [`00bf1c3c`](#insn-00bf1c3c) 範囲 `[['00bf1c3c', '00bf1c47']]`
  - `CONDITIONAL_JUMP` [`00bf1c44`](#insn-00bf1c44) → [`00bf1c08`](#insn-00bf1c08)
  - `FALL_THROUGH` [`00bf1c44`](#insn-00bf1c44) → [`00bf1c48`](#insn-00bf1c48)
- ブロック [`00bf1c48`](#insn-00bf1c48) 範囲 `[['00bf1c48', '00bf1c53']]`
  - `CONDITIONAL_JUMP` [`00bf1c50`](#insn-00bf1c50) → [`00bf1c08`](#insn-00bf1c08)
  - `FALL_THROUGH` [`00bf1c50`](#insn-00bf1c50) → [`00bf1c54`](#insn-00bf1c54)
- ブロック [`00bf1c54`](#insn-00bf1c54) 範囲 `[['00bf1c54', '00bf1c67']]`
  - `CONDITIONAL_JUMP` [`00bf1c64`](#insn-00bf1c64) → [`00bf1c0c`](#insn-00bf1c0c)
  - `FALL_THROUGH` [`00bf1c64`](#insn-00bf1c64) → [`00bf1c68`](#insn-00bf1c68)
- ブロック [`00bf1c68`](#insn-00bf1c68) 範囲 `[['00bf1c68', '00bf1c77']]`
  - `CONDITIONAL_JUMP` [`00bf1c74`](#insn-00bf1c74) → [`00bf1c3c`](#insn-00bf1c3c)
  - `FALL_THROUGH` [`00bf1c74`](#insn-00bf1c74) → [`00bf1c78`](#insn-00bf1c78)
- ブロック [`00bf1c78`](#insn-00bf1c78) 範囲 `[['00bf1c78', '00bf1c7b']]`
  - `UNCONDITIONAL_JUMP` [`00bf1c78`](#insn-00bf1c78) → [`00bf1c08`](#insn-00bf1c08)

## 命令位置別の参照

- [`00bf1bb0`](#insn-00bf1bb0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1bb4`](#insn-00bf1bb4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1bb8`](#insn-00bf1bb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1bbc`](#insn-00bf1bbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1be0`](#insn-00bf1be0) → [`00bf1bec`](#insn-00bf1bec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1be8`](#insn-00bf1be8) → [`00bf1c18`](#insn-00bf1c18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1bf0`](#insn-00bf1bf0) → [`00bf1c18`](#insn-00bf1c18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1c04`](#insn-00bf1c04) → [`00bf1c34`](#insn-00bf1c34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1c1c`](#insn-00bf1c1c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1c20`](#insn-00bf1c20) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1c24`](#insn-00bf1c24) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1c28`](#insn-00bf1c28) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1c44`](#insn-00bf1c44) → [`00bf1c08`](#insn-00bf1c08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1c4c`](#insn-00bf1c4c) → [`00c57bd0`](../00c57/00c57bd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57bd0` · 推定シンボル `None` · 推定型 `None`
- [`00bf1c50`](#insn-00bf1c50) → [`00bf1c08`](#insn-00bf1c08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1c60`](#insn-00bf1c60) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bf1c64`](#insn-00bf1c64) → [`00bf1c0c`](#insn-00bf1c0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1c74`](#insn-00bf1c74) → [`00bf1c3c`](#insn-00bf1c3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1c78`](#insn-00bf1c78) → [`00bf1c08`](#insn-00bf1c08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf1bb0`](#insn-00bf1bb0)

~~~json
{
  "source": "00bf1bb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1bb4`](#insn-00bf1bb4)

~~~json
{
  "source": "00bf1bb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1bb8`](#insn-00bf1bb8)

~~~json
{
  "source": "00bf1bb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1bbc`](#insn-00bf1bbc)

~~~json
{
  "source": "00bf1bbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1be0`](#insn-00bf1be0)

~~~json
{
  "source": "00bf1be0",
  "target": "00bf1bec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1be8`](#insn-00bf1be8)

~~~json
{
  "source": "00bf1be8",
  "target": "00bf1c18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1bf0`](#insn-00bf1bf0)

~~~json
{
  "source": "00bf1bf0",
  "target": "00bf1c18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1c04`](#insn-00bf1c04)

~~~json
{
  "source": "00bf1c04",
  "target": "00bf1c34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1c1c`](#insn-00bf1c1c)

~~~json
{
  "source": "00bf1c1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1c20`](#insn-00bf1c20)

~~~json
{
  "source": "00bf1c20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1c24`](#insn-00bf1c24)

~~~json
{
  "source": "00bf1c24",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1c28`](#insn-00bf1c28)

~~~json
{
  "source": "00bf1c28",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1c44`](#insn-00bf1c44)

~~~json
{
  "source": "00bf1c44",
  "target": "00bf1c08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1c4c`](#insn-00bf1c4c)

~~~json
{
  "source": "00bf1c4c",
  "target": "00c57bd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf1c50`](#insn-00bf1c50)

~~~json
{
  "source": "00bf1c50",
  "target": "00bf1c08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1c60`](#insn-00bf1c60)

~~~json
{
  "source": "00bf1c60",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf1c64`](#insn-00bf1c64)

~~~json
{
  "source": "00bf1c64",
  "target": "00bf1c0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1c74`](#insn-00bf1c74)

~~~json
{
  "source": "00bf1c74",
  "target": "00bf1c3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1c78`](#insn-00bf1c78)

~~~json
{
  "source": "00bf1c78",
  "target": "00bf1c08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
