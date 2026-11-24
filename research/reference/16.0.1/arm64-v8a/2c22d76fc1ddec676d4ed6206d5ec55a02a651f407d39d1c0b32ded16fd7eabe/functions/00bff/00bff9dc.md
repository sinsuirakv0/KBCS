# 00bff9dc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bff5b4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff5b4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-dea141d6c7cf5e8bbcda67cff69d8cfb)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bffa78`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffa78.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0042.md#compare-76f1ca43dbd212d5429f063c7976451c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bff9dc",
  "name": "_ZNSt6__ndk19basic_iosIwNS_11char_traitsIwEEE7copyfmtERKS3_",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6e98b28c97b222eb442b40729b3cd923bff1c326909c559ca050449c40d68a10",
  "source_text_sha256": "6e98b28c97b222eb442b40729b3cd923bff1c326909c559ca050449c40d68a10",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bff9dc",
        "00bffa57"
      ]
    ],
    "bytes_sha256": "fbc5f490664dd6fe7c30835b57446a8280014e2a79b78448e1121fa0b41347b7",
    "instruction_count": 31,
    "instruction_bytes": 124,
    "body_bytes": 124,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c582a0](../00c58/00c582a0.md)
- [00c5e2d0](../00c5e/00c5e2d0.md)
- [00c5e310](../00c5e/00c5e310.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 674 bytes

~~~c

long _ZNSt6__ndk19basic_iosIwNS_11char_traitsIwEEE7copyfmtERKS3_(long param_1,long param_2)

{
  undefined4 uVar1;
  
  if (param_1 != param_2) {
    _ZNSt6__ndk18ios_base16__call_callbacksENS0_5eventE(param_1,0);
    _ZNSt6__ndk18ios_base7copyfmtERKS0_(param_1,param_2);
    uVar1 = *(undefined4 *)(param_2 + 0x90);
    *(undefined8 *)(param_1 + 0x88) = *(undefined8 *)(param_2 + 0x88);
    *(undefined4 *)(param_1 + 0x90) = uVar1;
    _ZNSt6__ndk18ios_base16__call_callbacksENS0_5eventE(param_1,2);
    *(undefined4 *)(param_1 + 0x24) = *(undefined4 *)(param_2 + 0x24);
    _ZNSt6__ndk18ios_base5clearEj(param_1,*(undefined4 *)(param_1 + 0x20));
  }
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bff9dc"></a> `00bff9dc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bff9e0"></a> `00bff9e0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bff9e4"></a> `00bff9e4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bff9e8"></a> `00bff9e8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bff9ec"></a> `00bff9ec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bff9f0"></a> `00bff9f0` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-00bff9f4"></a> `00bff9f4` | `80 02 00 54` | b.eq 0x00bffa44 | `CONDITIONAL_JUMP`
<a id="insn-00bff9f8"></a> `00bff9f8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bff9fc"></a> `00bff9fc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bffa00"></a> `00bffa00` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bffa04"></a> `00bffa04` | `33 7a 01 94` | bl 0x00c5e2d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bffa08"></a> `00bffa08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bffa0c"></a> `00bffa0c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bffa10"></a> `00bffa10` | `40 7a 01 94` | bl 0x00c5e310 | `UNCONDITIONAL_CALL`
<a id="insn-00bffa14"></a> `00bffa14` | `88 46 40 f9` | ldr x8,[x20, #0x88] | `FALL_THROUGH`
<a id="insn-00bffa18"></a> `00bffa18` | `89 92 40 b9` | ldr w9,[x20, #0x90] | `FALL_THROUGH`
<a id="insn-00bffa1c"></a> `00bffa1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bffa20"></a> `00bffa20` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-00bffa24"></a> `00bffa24` | `68 46 00 f9` | str x8,[x19, #0x88] | `FALL_THROUGH`
<a id="insn-00bffa28"></a> `00bffa28` | `69 92 00 b9` | str w9,[x19, #0x90] | `FALL_THROUGH`
<a id="insn-00bffa2c"></a> `00bffa2c` | `29 7a 01 94` | bl 0x00c5e2d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bffa30"></a> `00bffa30` | `88 26 40 b9` | ldr w8,[x20, #0x24] | `FALL_THROUGH`
<a id="insn-00bffa34"></a> `00bffa34` | `61 22 40 b9` | ldr w1,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bffa38"></a> `00bffa38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bffa3c"></a> `00bffa3c` | `68 26 00 b9` | str w8,[x19, #0x24] | `FALL_THROUGH`
<a id="insn-00bffa40"></a> `00bffa40` | `18 62 01 94` | bl 0x00c582a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bffa44"></a> `00bffa44` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bffa48"></a> `00bffa48` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bffa4c"></a> `00bffa4c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bffa50"></a> `00bffa50` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bffa54"></a> `00bffa54` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bff9dc`](#insn-00bff9dc) 範囲 `[['00bff9dc', '00bff9f7']]`
  - `CONDITIONAL_JUMP` [`00bff9f4`](#insn-00bff9f4) → [`00bffa44`](#insn-00bffa44)
  - `FALL_THROUGH` [`00bff9f4`](#insn-00bff9f4) → [`00bff9f8`](#insn-00bff9f8)
- ブロック [`00bff9f8`](#insn-00bff9f8) 範囲 `[['00bff9f8', '00bffa43']]`
  - `FALL_THROUGH` [`00bffa40`](#insn-00bffa40) → [`00bffa44`](#insn-00bffa44)
- ブロック [`00bffa44`](#insn-00bffa44) 範囲 `[['00bffa44', '00bffa57']]`

## 命令位置別の参照

- [`00bff9e0`](#insn-00bff9e0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff9e4`](#insn-00bff9e4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff9f4`](#insn-00bff9f4) → [`00bffa44`](#insn-00bffa44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffa04`](#insn-00bffa04) → [`00c5e2d0`](../00c5e/00c5e2d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e2d0` · 推定シンボル `None` · 推定型 `None`
- [`00bffa10`](#insn-00bffa10) → [`00c5e310`](../00c5e/00c5e310.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e310` · 推定シンボル `None` · 推定型 `None`
- [`00bffa2c`](#insn-00bffa2c) → [`00c5e2d0`](../00c5e/00c5e2d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e2d0` · 推定シンボル `None` · 推定型 `None`
- [`00bffa40`](#insn-00bffa40) → [`00c582a0`](../00c58/00c582a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c582a0` · 推定シンボル `None` · 推定型 `None`
- [`00bffa48`](#insn-00bffa48) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffa4c`](#insn-00bffa4c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bff9e0`](#insn-00bff9e0)

~~~json
{
  "source": "00bff9e0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff9e4`](#insn-00bff9e4)

~~~json
{
  "source": "00bff9e4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff9f4`](#insn-00bff9f4)

~~~json
{
  "source": "00bff9f4",
  "target": "00bffa44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffa04`](#insn-00bffa04)

~~~json
{
  "source": "00bffa04",
  "target": "00c5e2d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffa10`](#insn-00bffa10)

~~~json
{
  "source": "00bffa10",
  "target": "00c5e310",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffa2c`](#insn-00bffa2c)

~~~json
{
  "source": "00bffa2c",
  "target": "00c5e2d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffa40`](#insn-00bffa40)

~~~json
{
  "source": "00bffa40",
  "target": "00c582a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffa48`](#insn-00bffa48)

~~~json
{
  "source": "00bffa48",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffa4c`](#insn-00bffa4c)

~~~json
{
  "source": "00bffa4c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
