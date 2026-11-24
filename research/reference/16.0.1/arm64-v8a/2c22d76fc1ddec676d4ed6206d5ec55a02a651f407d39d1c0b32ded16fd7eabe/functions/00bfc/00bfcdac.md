# 00bfcdac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfc984`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc984.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-2db143deb7df15f56e2a0b895a3789ed)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfce48`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfce48.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0086.md#compare-09016db4153ca1af830adf8aa909d2d0)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfcdac",
  "name": "FUN_00bfcdac",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "25a41377a1599c753dc9f682c7c56f21ec4a8305a6d6b227c4ba34b6820a157e",
  "source_text_sha256": "25a41377a1599c753dc9f682c7c56f21ec4a8305a6d6b227c4ba34b6820a157e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfcdac",
        "00bfce6b"
      ]
    ],
    "bytes_sha256": "0171d60a15b862899bc9289238b187761f039bce916bc81cb30d1f712796da72",
    "instruction_count": 48,
    "instruction_bytes": 192,
    "body_bytes": 192,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00bfcda4](../00bfc/00bfcda4.md)

## 呼び出し先

- [00c58270](../00c58/00c58270.md)
- [00c58280](../00c58/00c58280.md)
- [00c58290](../00c58/00c58290.md)
- [00c582a0](../00c58/00c582a0.md)
- [00c59dd0](../00c59/00c59dd0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1002 bytes

~~~c

long * FUN_00bfcdac(long *param_1,undefined8 param_2)

{
  long lVar1;
  long *plVar2;
  undefined1 auStack_30 [8];
  char local_28 [4];
  uint local_24;
  
  local_24 = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_28,param_1,0);
  if (local_28[0] != '\0') {
    _ZNKSt6__ndk18ios_base6getlocEv(auStack_30,(long)param_1 + *(long *)(*param_1 + -0x18));
    plVar2 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                               (auStack_30,
                                PTR__ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9bb10
                               );
    lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
    (**(code **)(*plVar2 + 0x40))(plVar2,*(undefined8 *)(lVar1 + 0x28),0,lVar1,&local_24,param_2);
    _ZNSt6__ndk16localeD1Ev(auStack_30);
    lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
    _ZNSt6__ndk18ios_base5clearEj(lVar1,*(uint *)(lVar1 + 0x20) | local_24);
  }
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfcdac"></a> `00bfcdac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfcdb0"></a> `00bfcdb0` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bfcdb4"></a> `00bfcdb4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfcdb8"></a> `00bfcdb8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfcdbc"></a> `00bfcdbc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bfcdc0"></a> `00bfcdc0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfcdc4"></a> `00bfcdc4` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bfcdc8"></a> `00bfcdc8` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfcdcc"></a> `00bfcdcc` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfcdd0"></a> `00bfcdd0` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00bfcdd4"></a> `00bfcdd4` | `bf c3 1f b8` | stur wzr,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfcdd8"></a> `00bfcdd8` | `fe 73 01 94` | bl 0x00c59dd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcddc"></a> `00bfcddc` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bfcde0"></a> `00bfcde0` | `a8 03 00 34` | cbz w8,0x00bfce54 | `CONDITIONAL_JUMP`
<a id="insn-00bfcde4"></a> `00bfcde4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfcde8"></a> `00bfcde8` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfcdec"></a> `00bfcdec` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00bfcdf0"></a> `00bfcdf0` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bfcdf4"></a> `00bfcdf4` | `1f 6d 01 94` | bl 0x00c58270 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcdf8"></a> `00bfcdf8` | `e1 04 00 f0` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bfcdfc"></a> `00bfcdfc` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bfce00"></a> `00bfce00` | `21 88 45 f9` | ldr x1,[x1, #0xb10] | `FALL_THROUGH`
<a id="insn-00bfce04"></a> `00bfce04` | `1f 6d 01 94` | bl 0x00c58280 | `UNCONDITIONAL_CALL`
<a id="insn-00bfce08"></a> `00bfce08` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfce0c"></a> `00bfce0c` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00bfce10"></a> `00bfce10` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfce14"></a> `00bfce14` | `63 02 08 8b` | add x3,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfce18"></a> `00bfce18` | `28 21 40 f9` | ldr x8,[x9, #0x40] | `FALL_THROUGH`
<a id="insn-00bfce1c"></a> `00bfce1c` | `61 14 40 f9` | ldr x1,[x3, #0x28] | `FALL_THROUGH`
<a id="insn-00bfce20"></a> `00bfce20` | `a4 13 00 d1` | sub x4,x29,#0x4 | `FALL_THROUGH`
<a id="insn-00bfce24"></a> `00bfce24` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bfce28"></a> `00bfce28` | `e5 03 14 aa` | mov x5,x20 | `FALL_THROUGH`
<a id="insn-00bfce2c"></a> `00bfce2c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfce30"></a> `00bfce30` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bfce34"></a> `00bfce34` | `17 6d 01 94` | bl 0x00c58290 | `UNCONDITIONAL_CALL`
<a id="insn-00bfce38"></a> `00bfce38` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfce3c"></a> `00bfce3c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfce40"></a> `00bfce40` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfce44"></a> `00bfce44` | `a8 c3 5f b8` | ldur w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfce48"></a> `00bfce48` | `09 20 40 b9` | ldr w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfce4c"></a> `00bfce4c` | `21 01 08 2a` | orr w1,w9,w8 | `FALL_THROUGH`
<a id="insn-00bfce50"></a> `00bfce50` | `14 6d 01 94` | bl 0x00c582a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfce54"></a> `00bfce54` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfce58"></a> `00bfce58` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfce5c"></a> `00bfce5c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfce60"></a> `00bfce60` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bfce64"></a> `00bfce64` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfce68"></a> `00bfce68` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfcdac`](#insn-00bfcdac) 範囲 `[['00bfcdac', '00bfcde3']]`
  - `CONDITIONAL_JUMP` [`00bfcde0`](#insn-00bfcde0) → [`00bfce54`](#insn-00bfce54)
  - `FALL_THROUGH` [`00bfcde0`](#insn-00bfcde0) → [`00bfcde4`](#insn-00bfcde4)
- ブロック [`00bfcde4`](#insn-00bfcde4) 範囲 `[['00bfcde4', '00bfce53']]`
  - `FALL_THROUGH` [`00bfce50`](#insn-00bfce50) → [`00bfce54`](#insn-00bfce54)
- ブロック [`00bfce54`](#insn-00bfce54) 範囲 `[['00bfce54', '00bfce6b']]`

## 命令位置別の参照

- [`00bfcdb4`](#insn-00bfcdb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcdb8`](#insn-00bfcdb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcdd4`](#insn-00bfcdd4) → `Stack[-0x24]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcdd8`](#insn-00bfcdd8) → [`00c59dd0`](../00c59/00c59dd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59dd0` · 推定シンボル `None` · 推定型 `None`
- [`00bfcddc`](#insn-00bfcddc) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcde0`](#insn-00bfcde0) → [`00bfce54`](#insn-00bfce54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcdf4`](#insn-00bfcdf4) → [`00c58270`](../00c58/00c58270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58270` · 推定シンボル `None` · 推定型 `None`
- [`00bfce00`](#insn-00bfce00) → `00c9bb10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfce00`](#insn-00bfce00) → `01127b78`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00bfce04`](#insn-00bfce04) → [`00c58280`](../00c58/00c58280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58280` · 推定シンボル `None` · 推定型 `None`
- [`00bfce34`](#insn-00bfce34) → [`00c58290`](../00c58/00c58290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58290` · 推定シンボル `None` · 推定型 `None`
- [`00bfce44`](#insn-00bfce44) → `Stack[-0x24]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfce50`](#insn-00bfce50) → [`00c582a0`](../00c58/00c582a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c582a0` · 推定シンボル `None` · 推定型 `None`
- [`00bfce58`](#insn-00bfce58) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfce5c`](#insn-00bfce5c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfcdb4`](#insn-00bfcdb4)

~~~json
{
  "source": "00bfcdb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcdb8`](#insn-00bfcdb8)

~~~json
{
  "source": "00bfcdb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcdd4`](#insn-00bfcdd4)

~~~json
{
  "source": "00bfcdd4",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcdd8`](#insn-00bfcdd8)

~~~json
{
  "source": "00bfcdd8",
  "target": "00c59dd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcddc`](#insn-00bfcddc)

~~~json
{
  "source": "00bfcddc",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcde0`](#insn-00bfcde0)

~~~json
{
  "source": "00bfcde0",
  "target": "00bfce54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcdf4`](#insn-00bfcdf4)

~~~json
{
  "source": "00bfcdf4",
  "target": "00c58270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfce00`](#insn-00bfce00)

~~~json
{
  "source": "00bfce00",
  "target": "00c9bb10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bb10",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfce00`](#insn-00bfce00)

~~~json
{
  "source": "00bfce00",
  "target": "01127b78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127b78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfce04`](#insn-00bfce04)

~~~json
{
  "source": "00bfce04",
  "target": "00c58280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfce34`](#insn-00bfce34)

~~~json
{
  "source": "00bfce34",
  "target": "00c58290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfce44`](#insn-00bfce44)

~~~json
{
  "source": "00bfce44",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfce50`](#insn-00bfce50)

~~~json
{
  "source": "00bfce50",
  "target": "00c582a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfce58`](#insn-00bfce58)

~~~json
{
  "source": "00bfce58",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfce5c`](#insn-00bfce5c)

~~~json
{
  "source": "00bfce5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
