# 004adbdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `0048ad44`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048ad44.md) · 移動量 `+0x22e98`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0007.md#compare-b667c15da08afec3b9fc2f11a95a6ffe)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `004adc1c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004adc1c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0007.md#compare-4f1597f25c2a73a9353a32cbc40eb5d8)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004adbdc",
  "name": "_ZN5Botan9X509_TimeC1ERKNSt6__ndk16chrono10time_pointINS2_12system_clockENS2_8durationIxNS1_5ratioILl1ELl1000000EEEEEEE",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "af66e4a8d7157c1dab53fbedfb73a780f0133f68fcd864e3e11354f8814a0f54",
  "source_text_sha256": "af66e4a8d7157c1dab53fbedfb73a780f0133f68fcd864e3e11354f8814a0f54",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004adbdc",
        "004adc83"
      ]
    ],
    "bytes_sha256": "95b45b0bd5c26e3c0c0cf3e2487bf8d399a1d97c83f34d500b61641c255c409d",
    "instruction_count": 42,
    "instruction_bytes": 168,
    "body_bytes": 168,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c59670](../00c59/00c59670.md)

## 呼び出し先

- [00c57ae0](../00c57/00c57ae0.md)
- [00c585a0](../00c58/00c585a0.md)
- [00c585b0](../00c58/00c585b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1245 bytes

~~~c

void _ZN5Botan9X509_TimeC1ERKNSt6__ndk16chrono10time_pointINS2_12system_clockENS2_8durationIxNS1_5ratioILl1ELl1000000EEEEEEE
               (long *param_1,undefined8 param_2)

{
  long lVar1;
  undefined4 uVar2;
  undefined1 auVar3 [16];
  undefined1 local_70 [16];
  int local_60;
  int iStack_5c;
  time_t local_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  *param_1 = (long)(PTR__ZTVN5Botan9X509_TimeE_00c9a9b0 + 0x10);
  param_1[1] = 0;
  param_1[2] = 0;
  param_1[3] = 0;
  *(undefined4 *)(param_1 + 4) = 0xff00;
  local_30 = _ZNSt6__ndk16chrono12system_clock9to_time_tERKNS0_10time_pointIS1_NS0_8durationIxNS_5ratioILl1ELl1000000EEEEEEE
                       (param_2);
  gmtime_r(&local_30,(tm *)local_70);
  auVar3 = NEON_rev64(local_70,4);
  *(uint *)(param_1 + 1) = iStack_5c + 0x76cU;
  *(int *)((long)param_1 + 0xc) = local_60 + 1;
  auVar3 = NEON_ext(auVar3,auVar3,8,1);
  uVar2 = 0x17;
  if (0x801 < iStack_5c + 0x76cU) {
    uVar2 = 0x18;
  }
  *(undefined4 *)(param_1 + 4) = uVar2;
  param_1[3] = auVar3._8_8_;
  param_1[2] = auVar3._0_8_;
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004adbdc"></a> `004adbdc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-004adbe0"></a> `004adbe0` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004adbe4"></a> `004adbe4` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004adbe8"></a> `004adbe8` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-004adbec"></a> `004adbec` | `68 3f 00 b0` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-004adbf0"></a> `004adbf0` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004adbf4"></a> `004adbf4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004adbf8"></a> `004adbf8` | `08 d9 44 f9` | ldr x8,[x8, #0x9b0] | `FALL_THROUGH`
<a id="insn-004adbfc"></a> `004adbfc` | `89 16 40 f9` | ldr x9,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-004adc00"></a> `004adc00` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-004adc04"></a> `004adc04` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004adc08"></a> `004adc08` | `08 7c 00 a9` | stp x8,xzr,[x0] | `FALL_THROUGH`
<a id="insn-004adc0c"></a> `004adc0c` | `08 e0 9f 52` | mov w8,#0xff00 | `FALL_THROUGH`
<a id="insn-004adc10"></a> `004adc10` | `1f 7c 01 a9` | stp xzr,xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004adc14"></a> `004adc14` | `08 20 00 b9` | str w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-004adc18"></a> `004adc18` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-004adc1c"></a> `004adc1c` | `61 aa 1e 94` | bl 0x00c585a0 | `UNCONDITIONAL_CALL`
<a id="insn-004adc20"></a> `004adc20` | `a0 03 1f f8` | stur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-004adc24"></a> `004adc24` | `a0 43 00 d1` | sub x0,x29,#0x10 | `FALL_THROUGH`
<a id="insn-004adc28"></a> `004adc28` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-004adc2c"></a> `004adc2c` | `61 aa 1e 94` | bl 0x00c585b0 | `UNCONDITIONAL_CALL`
<a id="insn-004adc30"></a> `004adc30` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-004adc34"></a> `004adc34` | `e9 23 42 29` | ldp w9,w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004adc38"></a> `004adc38` | `00 08 a0 4e` | rev64 v0.4S,v0.4S | `FALL_THROUGH`
<a id="insn-004adc3c"></a> `004adc3c` | `08 b1 1d 11` | add w8,w8,#0x76c | `FALL_THROUGH`
<a id="insn-004adc40"></a> `004adc40` | `29 05 00 11` | add w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-004adc44"></a> `004adc44` | `68 26 01 29` | stp w8,w9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-004adc48"></a> `004adc48` | `e9 02 80 52` | mov w9,#0x17 | `FALL_THROUGH`
<a id="insn-004adc4c"></a> `004adc4c` | `1f 05 20 71` | cmp w8,#0x801 | `FALL_THROUGH`
<a id="insn-004adc50"></a> `004adc50` | `00 40 00 6e` | ext v0.16B,v0.16B,v0.16B,0x8 | `FALL_THROUGH`
<a id="insn-004adc54"></a> `004adc54` | `28 95 89 1a` | cinc w8,w9,hi | `FALL_THROUGH`
<a id="insn-004adc58"></a> `004adc58` | `68 22 00 b9` | str w8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-004adc5c"></a> `004adc5c` | `60 06 80 3d` | str q0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-004adc60"></a> `004adc60` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-004adc64"></a> `004adc64` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004adc68"></a> `004adc68` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004adc6c"></a> `004adc6c` | `a1 00 00 54` | b.ne 0x004adc80 | `CONDITIONAL_JUMP`
<a id="insn-004adc70"></a> `004adc70` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004adc74"></a> `004adc74` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004adc78"></a> `004adc78` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-004adc7c"></a> `004adc7c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004adc80"></a> `004adc80` | `98 a7 1e 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004adbdc`](#insn-004adbdc) 範囲 `[['004adbdc', '004adc6f']]`
  - `CONDITIONAL_JUMP` [`004adc6c`](#insn-004adc6c) → [`004adc80`](#insn-004adc80)
  - `FALL_THROUGH` [`004adc6c`](#insn-004adc6c) → [`004adc70`](#insn-004adc70)
- ブロック [`004adc70`](#insn-004adc70) 範囲 `[['004adc70', '004adc7f']]`
- ブロック [`004adc80`](#insn-004adc80) 範囲 `[['004adc80', '004adc83']]`

## 命令位置別の参照

- [`004adbe0`](#insn-004adbe0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004adbe4`](#insn-004adbe4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004adbf8`](#insn-004adbf8) → `00c9a9b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004adc04`](#insn-004adc04) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004adc08`](#insn-004adc08) → `00c65f78`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[48]`
- [`004adc1c`](#insn-004adc1c) → [`00c585a0`](../00c58/00c585a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c585a0` · 推定シンボル `None` · 推定型 `None`
- [`004adc20`](#insn-004adc20) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004adc2c`](#insn-004adc2c) → [`00c585b0`](../00c58/00c585b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c585b0` · 推定シンボル `None` · 推定型 `None`
- [`004adc30`](#insn-004adc30) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004adc34`](#insn-004adc34) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004adc64`](#insn-004adc64) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004adc6c`](#insn-004adc6c) → [`004adc80`](#insn-004adc80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004adc70`](#insn-004adc70) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004adc74`](#insn-004adc74) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004adc80`](#insn-004adc80) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004adbe0`](#insn-004adbe0)

~~~json
{
  "source": "004adbe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004adbe4`](#insn-004adbe4)

~~~json
{
  "source": "004adbe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004adbf8`](#insn-004adbf8)

~~~json
{
  "source": "004adbf8",
  "target": "00c9a9b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9a9b0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004adc04`](#insn-004adc04)

~~~json
{
  "source": "004adc04",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004adc08`](#insn-004adc08)

~~~json
{
  "source": "004adc08",
  "target": "00c65f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c65f68",
  "offset": 16,
  "size": 48,
  "datatype": "undefined1[48]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004adc1c`](#insn-004adc1c)

~~~json
{
  "source": "004adc1c",
  "target": "00c585a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004adc20`](#insn-004adc20)

~~~json
{
  "source": "004adc20",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004adc2c`](#insn-004adc2c)

~~~json
{
  "source": "004adc2c",
  "target": "00c585b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004adc30`](#insn-004adc30)

~~~json
{
  "source": "004adc30",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004adc34`](#insn-004adc34)

~~~json
{
  "source": "004adc34",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004adc64`](#insn-004adc64)

~~~json
{
  "source": "004adc64",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004adc6c`](#insn-004adc6c)

~~~json
{
  "source": "004adc6c",
  "target": "004adc80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004adc70`](#insn-004adc70)

~~~json
{
  "source": "004adc70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004adc74`](#insn-004adc74)

~~~json
{
  "source": "004adc74",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004adc80`](#insn-004adc80)

~~~json
{
  "source": "004adc80",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
