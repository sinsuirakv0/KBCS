# 00bff5bc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bff194`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff194.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-e83ebe52356dcf31f33d6c625f32814b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bff658`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff658.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-b1e981bddc9f7a7c0805e610f6c9cde9)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bff5bc",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5seekpENS_4fposI9mbstate_tEE",
  "size": 172,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "96163f29d86071e42523ff44c895d095650a98a9f7f07903cb5a4c1d2c49d357",
  "source_text_sha256": "96163f29d86071e42523ff44c895d095650a98a9f7f07903cb5a4c1d2c49d357",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bff5bc",
        "00bff667"
      ]
    ],
    "bytes_sha256": "2222e7218a3617212864aa8e30a595ec99be9199f7a871094ba7f59c985cc9b1",
    "instruction_count": 43,
    "instruction_bytes": 172,
    "body_bytes": 172,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58260](../00c58/00c58260.md)
- [00c582a0](../00c58/00c582a0.md)
- [00c582b0](../00c58/00c582b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 811 bytes

~~~c

long * _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5seekpENS_4fposI9mbstate_tEE
                 (long *param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  long *plVar2;
  long extraout_x1;
  undefined1 auStack_40 [16];
  
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_(auStack_40,param_1);
  if (((*(byte *)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x20) & 5) == 0) &&
     (plVar2 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28),
     (**(code **)(*plVar2 + 0x28))(plVar2,param_2,param_3,0x10), extraout_x1 == -1)) {
    lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
    _ZNSt6__ndk18ios_base5clearEj(lVar1,*(uint *)(lVar1 + 0x20) | 4);
  }
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE6sentryD2Ev(auStack_40);
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bff5bc"></a> `00bff5bc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bff5c0"></a> `00bff5c0` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bff5c4"></a> `00bff5c4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bff5c8"></a> `00bff5c8` | `f5 13 00 f9` | str x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bff5cc"></a> `00bff5cc` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bff5d0"></a> `00bff5d0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bff5d4"></a> `00bff5d4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bff5d8"></a> `00bff5d8` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bff5dc"></a> `00bff5dc` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bff5e0"></a> `00bff5e0` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bff5e4"></a> `00bff5e4` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00bff5e8"></a> `00bff5e8` | `1e 63 01 94` | bl 0x00c58260 | `UNCONDITIONAL_CALL`
<a id="insn-00bff5ec"></a> `00bff5ec` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bff5f0"></a> `00bff5f0` | `aa 00 80 52` | mov w10,#0x5 | `FALL_THROUGH`
<a id="insn-00bff5f4"></a> `00bff5f4` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bff5f8"></a> `00bff5f8` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00bff5fc"></a> `00bff5fc` | `09 81 40 39` | ldrb w9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bff600"></a> `00bff600` | `3f 01 0a 6a` | tst w9,w10 | `FALL_THROUGH`
<a id="insn-00bff604"></a> `00bff604` | `01 02 00 54` | b.ne 0x00bff644 | `CONDITIONAL_JUMP`
<a id="insn-00bff608"></a> `00bff608` | `00 15 40 f9` | ldr x0,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bff60c"></a> `00bff60c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bff610"></a> `00bff610` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bff614"></a> `00bff614` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bff618"></a> `00bff618` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00bff61c"></a> `00bff61c` | `03 02 80 52` | mov w3,#0x10 | `FALL_THROUGH`
<a id="insn-00bff620"></a> `00bff620` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bff624"></a> `00bff624` | `3f 04 00 b1` | cmn x1,#0x1 | `FALL_THROUGH`
<a id="insn-00bff628"></a> `00bff628` | `e1 00 00 54` | b.ne 0x00bff644 | `CONDITIONAL_JUMP`
<a id="insn-00bff62c"></a> `00bff62c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bff630"></a> `00bff630` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bff634"></a> `00bff634` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bff638"></a> `00bff638` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bff63c"></a> `00bff63c` | `01 01 1e 32` | orr w1,w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bff640"></a> `00bff640` | `18 63 01 94` | bl 0x00c582a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bff644"></a> `00bff644` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bff648"></a> `00bff648` | `1a 63 01 94` | bl 0x00c582b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bff64c"></a> `00bff64c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bff650"></a> `00bff650` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bff654"></a> `00bff654` | `f5 13 40 f9` | ldr x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bff658"></a> `00bff658` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bff65c"></a> `00bff65c` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bff660"></a> `00bff660` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bff664"></a> `00bff664` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bff5bc`](#insn-00bff5bc) 範囲 `[['00bff5bc', '00bff607']]`
  - `CONDITIONAL_JUMP` [`00bff604`](#insn-00bff604) → [`00bff644`](#insn-00bff644)
  - `FALL_THROUGH` [`00bff604`](#insn-00bff604) → [`00bff608`](#insn-00bff608)
- ブロック [`00bff608`](#insn-00bff608) 範囲 `[['00bff608', '00bff62b']]`
  - `CONDITIONAL_JUMP` [`00bff628`](#insn-00bff628) → [`00bff644`](#insn-00bff644)
  - `FALL_THROUGH` [`00bff628`](#insn-00bff628) → [`00bff62c`](#insn-00bff62c)
- ブロック [`00bff62c`](#insn-00bff62c) 範囲 `[['00bff62c', '00bff643']]`
  - `FALL_THROUGH` [`00bff640`](#insn-00bff640) → [`00bff644`](#insn-00bff644)
- ブロック [`00bff644`](#insn-00bff644) 範囲 `[['00bff644', '00bff667']]`

## 命令位置別の参照

- [`00bff5c4`](#insn-00bff5c4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff5c8`](#insn-00bff5c8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff5cc`](#insn-00bff5cc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff5e8`](#insn-00bff5e8) → [`00c58260`](../00c58/00c58260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58260` · 推定シンボル `None` · 推定型 `None`
- [`00bff604`](#insn-00bff604) → [`00bff644`](#insn-00bff644) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff628`](#insn-00bff628) → [`00bff644`](#insn-00bff644) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff640`](#insn-00bff640) → [`00c582a0`](../00c58/00c582a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c582a0` · 推定シンボル `None` · 推定型 `None`
- [`00bff648`](#insn-00bff648) → [`00c582b0`](../00c58/00c582b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c582b0` · 推定シンボル `None` · 推定型 `None`
- [`00bff650`](#insn-00bff650) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff654`](#insn-00bff654) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff658`](#insn-00bff658) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bff5c4`](#insn-00bff5c4)

~~~json
{
  "source": "00bff5c4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff5c8`](#insn-00bff5c8)

~~~json
{
  "source": "00bff5c8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff5cc`](#insn-00bff5cc)

~~~json
{
  "source": "00bff5cc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff5e8`](#insn-00bff5e8)

~~~json
{
  "source": "00bff5e8",
  "target": "00c58260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bff604`](#insn-00bff604)

~~~json
{
  "source": "00bff604",
  "target": "00bff644",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff628`](#insn-00bff628)

~~~json
{
  "source": "00bff628",
  "target": "00bff644",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff640`](#insn-00bff640)

~~~json
{
  "source": "00bff640",
  "target": "00c582a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bff648`](#insn-00bff648)

~~~json
{
  "source": "00bff648",
  "target": "00c582b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bff650`](#insn-00bff650)

~~~json
{
  "source": "00bff650",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff654`](#insn-00bff654)

~~~json
{
  "source": "00bff654",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff658`](#insn-00bff658)

~~~json
{
  "source": "00bff658",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
