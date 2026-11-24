# 00bfb8dc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7ee94`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ee94.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0020.md#compare-7ea928567c39733de5ee232b99559666)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfbd04`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbd04.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-ee21bf2955504fd85de9da4306f1ea19)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfb8dc",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6snextcEv",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "29df578467124302e54f80ac5d43c6f1de7336d9444012fd8f8db34a80765029",
  "source_text_sha256": "29df578467124302e54f80ac5d43c6f1de7336d9444012fd8f8db34a80765029",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfb8dc",
        "00bfb95f"
      ]
    ],
    "bytes_sha256": "0814b993bf392c0570fe6d76a5105d814643dec241838e640f6efc9d58b4701f",
    "instruction_count": 33,
    "instruction_bytes": 132,
    "body_bytes": 132,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 764 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6snextcEv(long *param_1)

{
  ulong uVar1;
  byte *pbVar2;
  
  if ((byte *)param_1[3] == (byte *)param_1[4]) {
    uVar1 = (**(code **)(*param_1 + 0x50))();
    if ((int)uVar1 == -1) {
      return uVar1;
    }
    pbVar2 = (byte *)param_1[3];
    if (pbVar2 == (byte *)param_1[4]) goto LAB_00bfb938;
  }
  else {
    pbVar2 = (byte *)param_1[3] + 1;
    param_1[3] = (long)pbVar2;
    if (pbVar2 == (byte *)param_1[4]) {
LAB_00bfb938:
                    /* WARNING: Could not recover jumptable at 0x00bfb94c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      uVar1 = (**(code **)(*param_1 + 0x48))();
      return uVar1;
    }
  }
  return (ulong)*pbVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfb8dc"></a> `00bfb8dc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfb8e0"></a> `00bfb8e0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfb8e4"></a> `00bfb8e4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfb8e8"></a> `00bfb8e8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfb8ec"></a> `00bfb8ec` | `09 a0 41 a9` | ldp x9,x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfb8f0"></a> `00bfb8f0` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bfb8f4"></a> `00bfb8f4` | `e0 00 00 54` | b.eq 0x00bfb910 | `CONDITIONAL_JUMP`
<a id="insn-00bfb8f8"></a> `00bfb8f8` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bfb8fc"></a> `00bfb8fc` | `09 0c 00 f9` | str x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfb900"></a> `00bfb900` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bfb904"></a> `00bfb904` | `a0 01 00 54` | b.eq 0x00bfb938 | `CONDITIONAL_JUMP`
<a id="insn-00bfb908"></a> `00bfb908` | `20 01 40 39` | ldrb w0,[x9] | `FALL_THROUGH`
<a id="insn-00bfb90c"></a> `00bfb90c` | `11 00 00 14` | b 0x00bfb950 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfb910"></a> `00bfb910` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfb914"></a> `00bfb914` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfb918"></a> `00bfb918` | `08 29 40 f9` | ldr x8,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00bfb91c"></a> `00bfb91c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfb920"></a> `00bfb920` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfb924"></a> `00bfb924` | `60 01 00 54` | b.eq 0x00bfb950 | `CONDITIONAL_JUMP`
<a id="insn-00bfb928"></a> `00bfb928` | `69 a2 41 a9` | ldp x9,x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bfb92c"></a> `00bfb92c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfb930"></a> `00bfb930` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bfb934"></a> `00bfb934` | `a1 fe ff 54` | b.ne 0x00bfb908 | `CONDITIONAL_JUMP`
<a id="insn-00bfb938"></a> `00bfb938` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfb93c"></a> `00bfb93c` | `10 25 40 f9` | ldr x16,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00bfb940"></a> `00bfb940` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfb944"></a> `00bfb944` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfb948"></a> `00bfb948` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfb94c"></a> `00bfb94c` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00bfb950"></a> `00bfb950` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfb954"></a> `00bfb954` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfb958"></a> `00bfb958` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfb95c"></a> `00bfb95c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfb8dc`](#insn-00bfb8dc) 範囲 `[['00bfb8dc', '00bfb8f7']]`
  - `CONDITIONAL_JUMP` [`00bfb8f4`](#insn-00bfb8f4) → [`00bfb910`](#insn-00bfb910)
  - `FALL_THROUGH` [`00bfb8f4`](#insn-00bfb8f4) → [`00bfb8f8`](#insn-00bfb8f8)
- ブロック [`00bfb8f8`](#insn-00bfb8f8) 範囲 `[['00bfb8f8', '00bfb907']]`
  - `CONDITIONAL_JUMP` [`00bfb904`](#insn-00bfb904) → [`00bfb938`](#insn-00bfb938)
  - `FALL_THROUGH` [`00bfb904`](#insn-00bfb904) → [`00bfb908`](#insn-00bfb908)
- ブロック [`00bfb908`](#insn-00bfb908) 範囲 `[['00bfb908', '00bfb90f']]`
  - `UNCONDITIONAL_JUMP` [`00bfb90c`](#insn-00bfb90c) → [`00bfb950`](#insn-00bfb950)
- ブロック [`00bfb910`](#insn-00bfb910) 範囲 `[['00bfb910', '00bfb927']]`
  - `CONDITIONAL_JUMP` [`00bfb924`](#insn-00bfb924) → [`00bfb950`](#insn-00bfb950)
  - `FALL_THROUGH` [`00bfb924`](#insn-00bfb924) → [`00bfb928`](#insn-00bfb928)
- ブロック [`00bfb928`](#insn-00bfb928) 範囲 `[['00bfb928', '00bfb937']]`
  - `CONDITIONAL_JUMP` [`00bfb934`](#insn-00bfb934) → [`00bfb908`](#insn-00bfb908)
  - `FALL_THROUGH` [`00bfb934`](#insn-00bfb934) → [`00bfb938`](#insn-00bfb938)
- ブロック [`00bfb938`](#insn-00bfb938) 範囲 `[['00bfb938', '00bfb94f']]`
- ブロック [`00bfb950`](#insn-00bfb950) 範囲 `[['00bfb950', '00bfb95f']]`

## 命令位置別の参照

- [`00bfb8e0`](#insn-00bfb8e0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb8e4`](#insn-00bfb8e4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb8f4`](#insn-00bfb8f4) → [`00bfb910`](#insn-00bfb910) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb904`](#insn-00bfb904) → [`00bfb938`](#insn-00bfb938) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb90c`](#insn-00bfb90c) → [`00bfb950`](#insn-00bfb950) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb924`](#insn-00bfb924) → [`00bfb950`](#insn-00bfb950) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb934`](#insn-00bfb934) → [`00bfb908`](#insn-00bfb908) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb940`](#insn-00bfb940) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb944`](#insn-00bfb944) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb950`](#insn-00bfb950) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb954`](#insn-00bfb954) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfb8e0`](#insn-00bfb8e0)

~~~json
{
  "source": "00bfb8e0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb8e4`](#insn-00bfb8e4)

~~~json
{
  "source": "00bfb8e4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb8f4`](#insn-00bfb8f4)

~~~json
{
  "source": "00bfb8f4",
  "target": "00bfb910",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb904`](#insn-00bfb904)

~~~json
{
  "source": "00bfb904",
  "target": "00bfb938",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb90c`](#insn-00bfb90c)

~~~json
{
  "source": "00bfb90c",
  "target": "00bfb950",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb924`](#insn-00bfb924)

~~~json
{
  "source": "00bfb924",
  "target": "00bfb950",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb934`](#insn-00bfb934)

~~~json
{
  "source": "00bfb934",
  "target": "00bfb908",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb940`](#insn-00bfb940)

~~~json
{
  "source": "00bfb940",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb944`](#insn-00bfb944)

~~~json
{
  "source": "00bfb944",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb950`](#insn-00bfb950)

~~~json
{
  "source": "00bfb950",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb954`](#insn-00bfb954)

~~~json
{
  "source": "00bfb954",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
