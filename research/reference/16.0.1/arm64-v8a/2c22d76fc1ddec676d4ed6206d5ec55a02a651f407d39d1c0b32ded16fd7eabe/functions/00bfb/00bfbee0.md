# 00bfbee0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfbab8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbab8.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-e48bd63a5528c3ade746e473c6f33633)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfbf7c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbf7c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0086.md#compare-e597a5f3252055756429407e03f8cbbe)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbee0",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1ERKS3_",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "09a8cc77653294c0a11c15029357a46c59092dd21eedbe10c285a10486b02140",
  "source_text_sha256": "09a8cc77653294c0a11c15029357a46c59092dd21eedbe10c285a10486b02140",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfbee0",
        "00bfbf37"
      ]
    ],
    "bytes_sha256": "185c18c363cfac06d0bf6f0d70b4c73fe390652591aa34a6740f950e76be24e1",
    "instruction_count": 22,
    "instruction_bytes": 88,
    "body_bytes": 88,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a7d0](../00c5a/00c5a7d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 585 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1ERKS3_(long *param_1,long param_2)

{
  long lVar1;
  
  *param_1 = (long)(PTR__ZTVNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEE_00c9b848 + 0x10);
  _ZNSt6__ndk16localeC1ERKS0_(param_1 + 1,param_2 + 8);
  lVar1 = *(long *)(param_2 + 0x10);
  param_1[3] = *(long *)(param_2 + 0x18);
  param_1[2] = lVar1;
  lVar1 = *(long *)(param_2 + 0x20);
  param_1[5] = *(long *)(param_2 + 0x28);
  param_1[4] = lVar1;
  lVar1 = *(long *)(param_2 + 0x30);
  param_1[7] = *(long *)(param_2 + 0x38);
  param_1[6] = lVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfbee0"></a> `00bfbee0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfbee4"></a> `00bfbee4` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfbee8"></a> `00bfbee8` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbeec"></a> `00bfbeec` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfbef0"></a> `00bfbef0` | `08 05 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bfbef4"></a> `00bfbef4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bfbef8"></a> `00bfbef8` | `21 20 00 91` | add x1,x1,#0x8 | `FALL_THROUGH`
<a id="insn-00bfbefc"></a> `00bfbefc` | `08 25 44 f9` | ldr x8,[x8, #0x848] | `FALL_THROUGH`
<a id="insn-00bfbf00"></a> `00bfbf00` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bfbf04"></a> `00bfbf04` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bfbf08"></a> `00bfbf08` | `08 84 00 f8` | str x8,[x0], #0x8 | `FALL_THROUGH`
<a id="insn-00bfbf0c"></a> `00bfbf0c` | `31 7a 01 94` | bl 0x00c5a7d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfbf10"></a> `00bfbf10` | `60 06 c0 3d` | ldr q0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbf14"></a> `00bfbf14` | `80 06 80 3d` | str q0,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbf18"></a> `00bfbf18` | `60 0a c0 3d` | ldr q0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bfbf1c"></a> `00bfbf1c` | `80 0a 80 3d` | str q0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00bfbf20"></a> `00bfbf20` | `60 0e c0 3d` | ldr q0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00bfbf24"></a> `00bfbf24` | `80 0e 80 3d` | str q0,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00bfbf28"></a> `00bfbf28` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbf2c"></a> `00bfbf2c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfbf30"></a> `00bfbf30` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfbf34"></a> `00bfbf34` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfbee0`](#insn-00bfbee0) 範囲 `[['00bfbee0', '00bfbf37']]`

## 命令位置別の参照

- [`00bfbee4`](#insn-00bfbee4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbee8`](#insn-00bfbee8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbefc`](#insn-00bfbefc) → `00c9b848`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfbf08`](#insn-00bfbf08) → `00c90cb0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`00bfbf0c`](#insn-00bfbf0c) → [`00c5a7d0`](../00c5a/00c5a7d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a7d0` · 推定シンボル `None` · 推定型 `None`
- [`00bfbf28`](#insn-00bfbf28) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbf2c`](#insn-00bfbf2c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfbee4`](#insn-00bfbee4)

~~~json
{
  "source": "00bfbee4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbee8`](#insn-00bfbee8)

~~~json
{
  "source": "00bfbee8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbefc`](#insn-00bfbefc)

~~~json
{
  "source": "00bfbefc",
  "target": "00c9b848",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b848",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfbf08`](#insn-00bfbf08)

~~~json
{
  "source": "00bfbf08",
  "target": "00c90cb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90ca0",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bfbf0c`](#insn-00bfbf0c)

~~~json
{
  "source": "00bfbf0c",
  "target": "00c5a7d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfbf28`](#insn-00bfbf28)

~~~json
{
  "source": "00bfbf28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbf2c`](#insn-00bfbf2c)

~~~json
{
  "source": "00bfbf2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
