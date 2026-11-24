# 00afcdb4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afcd70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afcd70.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0066.md#compare-cd0e67f54852dd7c6263b2519ec7dbfc)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b5cb38`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5cb38.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0061.md#compare-0e96b6db1f1e633dc79a4c0b9b46b9ae)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afcdb4",
  "name": "_ZN8firebase15CleanupNotifier11FindByOwnerEPv",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "95f82c14743897158d2e38d6baf3674df35470d5ab1ca161513d8e0f2380a231",
  "source_text_sha256": "95f82c14743897158d2e38d6baf3674df35470d5ab1ca161513d8e0f2380a231",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afcdb4",
        "00afce43"
      ]
    ],
    "bytes_sha256": "cd66803bf7176c0eec13ba0854c9307b0a071ccdfd105fce0d631b55fa230697",
    "instruction_count": 36,
    "instruction_bytes": 144,
    "body_bytes": 144,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bddd90](../00bdd/00bddd90.md)

## 呼び出し先

- [00bddc20](../00bdd/00bddc20.md)
- [00bddc30](../00bdd/00bddc30.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1334 bytes

~~~c

long _ZN8firebase15CleanupNotifier11FindByOwnerEPv(ulong param_1)

{
  long *plVar1;
  long *plVar2;
  long *plVar3;
  undefined8 uVar4;
  long lVar5;
  
  uVar4 = *(undefined8 *)
           PTR__ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E_00c1b998;
  _ZN8firebase5Mutex7AcquireEv(uVar4);
                    /* try { // try from 00afcddc to 00bfcde3 has its CatchHandler @ 00aff400 */
  if (*(long *)PTR__ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E_00c1b990 != 0) {
    plVar1 = (long *)(*(long *)
                       PTR__ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E_00c1b990 + 8)
    ;
    plVar3 = (long *)*plVar1;
    plVar2 = plVar1;
    if (plVar3 != (long *)0x0) {
      do {
        if ((ulong)plVar3[4] >= param_1) {
          plVar2 = plVar3;
        }
        plVar3 = (long *)plVar3[(ulong)plVar3[4] < param_1];
      } while (plVar3 != (long *)0x0);
                    /* try { // try from 00afce0c to 00bfce23 has its CatchHandler @ 00aff3fc */
      if ((plVar2 != plVar1) && ((ulong)plVar2[4] <= param_1)) {
        lVar5 = plVar2[5];
        goto LAB_00afce24;
      }
    }
  }
  lVar5 = 0;
LAB_00afce24:
                    /* try { // try from 00afce24 to 00bfcebf has its CatchHandler @ 00af5650 */
  _ZN8firebase5Mutex7ReleaseEv(uVar4);
  return lVar5;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afcdb4"></a> `00afcdb4` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afcdb8"></a> `00afcdb8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcdbc"></a> `00afcdbc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00afcdc0"></a> `00afcdc0` | `e8 08 00 f0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00afcdc4"></a> `00afcdc4` | `08 cd 44 f9` | ldr x8,[x8, #0x998] | `FALL_THROUGH`
<a id="insn-00afcdc8"></a> `00afcdc8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00afcdcc"></a> `00afcdcc` | `13 01 40 f9` | ldr x19,[x8] | `FALL_THROUGH`
<a id="insn-00afcdd0"></a> `00afcdd0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afcdd4"></a> `00afcdd4` | `93 83 03 94` | bl 0x00bddc20 | `UNCONDITIONAL_CALL`
<a id="insn-00afcdd8"></a> `00afcdd8` | `e8 08 00 f0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00afcddc"></a> `00afcddc` | `08 c9 44 f9` | ldr x8,[x8, #0x990] | `FALL_THROUGH`
<a id="insn-00afcde0"></a> `00afcde0` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00afcde4"></a> `00afcde4` | `e8 01 00 b4` | cbz x8,0x00afce20 | `CONDITIONAL_JUMP`
<a id="insn-00afcde8"></a> `00afcde8` | `0a 8d 40 f8` | ldr x10,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00afcdec"></a> `00afcdec` | `aa 01 00 b4` | cbz x10,0x00afce20 | `CONDITIONAL_JUMP`
<a id="insn-00afcdf0"></a> `00afcdf0` | `e9 03 08 aa` | mov x9,x8 | `FALL_THROUGH`
<a id="insn-00afcdf4"></a> `00afcdf4` | `4b 11 40 f9` | ldr x11,[x10, #0x20] | `FALL_THROUGH`
<a id="insn-00afcdf8"></a> `00afcdf8` | `7f 01 14 eb` | cmp x11,x20 | `FALL_THROUGH`
<a id="insn-00afcdfc"></a> `00afcdfc` | `eb 27 9f 1a` | cset w11,cc | `FALL_THROUGH`
<a id="insn-00afce00"></a> `00afce00` | `29 31 8a 9a` | csel x9,x9,x10,cc | `FALL_THROUGH`
<a id="insn-00afce04"></a> `00afce04` | `4a 59 6b f8` | ldr x10,[x10, w11, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00afce08"></a> `00afce08` | `6a ff ff b5` | cbnz x10,0x00afcdf4 | `CONDITIONAL_JUMP`
<a id="insn-00afce0c"></a> `00afce0c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00afce10"></a> `00afce10` | `80 00 00 54` | b.eq 0x00afce20 | `CONDITIONAL_JUMP`
<a id="insn-00afce14"></a> `00afce14` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00afce18"></a> `00afce18` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00afce1c"></a> `00afce1c` | `09 01 00 54` | b.ls 0x00afce3c | `CONDITIONAL_JUMP`
<a id="insn-00afce20"></a> `00afce20` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00afce24"></a> `00afce24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afce28"></a> `00afce28` | `82 83 03 94` | bl 0x00bddc30 | `UNCONDITIONAL_CALL`
<a id="insn-00afce2c"></a> `00afce2c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afce30"></a> `00afce30` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afce34"></a> `00afce34` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afce38"></a> `00afce38` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afce3c"></a> `00afce3c` | `34 15 40 f9` | ldr x20,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-00afce40"></a> `00afce40` | `f9 ff ff 17` | b 0x00afce24 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00afcdb4`](#insn-00afcdb4) 範囲 `[['00afcdb4', '00afcddb']]`
  - `FALL_THROUGH` [`00afcdd8`](#insn-00afcdd8) → [`00afcddc`](#insn-00afcddc)
- ブロック [`00afcddc`](#insn-00afcddc) 範囲 `[['00afcddc', '00afcde7']]`
  - `CONDITIONAL_JUMP` [`00afcde4`](#insn-00afcde4) → [`00afce20`](#insn-00afce20)
  - `FALL_THROUGH` [`00afcde4`](#insn-00afcde4) → [`00afcde8`](#insn-00afcde8)
- ブロック [`00afcde8`](#insn-00afcde8) 範囲 `[['00afcde8', '00afcdef']]`
  - `CONDITIONAL_JUMP` [`00afcdec`](#insn-00afcdec) → [`00afce20`](#insn-00afce20)
  - `FALL_THROUGH` [`00afcdec`](#insn-00afcdec) → [`00afcdf0`](#insn-00afcdf0)
- ブロック [`00afcdf0`](#insn-00afcdf0) 範囲 `[['00afcdf0', '00afcdf3']]`
  - `FALL_THROUGH` [`00afcdf0`](#insn-00afcdf0) → [`00afcdf4`](#insn-00afcdf4)
- ブロック [`00afcdf4`](#insn-00afcdf4) 範囲 `[['00afcdf4', '00afce0b']]`
  - `CONDITIONAL_JUMP` [`00afce08`](#insn-00afce08) → [`00afcdf4`](#insn-00afcdf4)
  - `FALL_THROUGH` [`00afce08`](#insn-00afce08) → [`00afce0c`](#insn-00afce0c)
- ブロック [`00afce0c`](#insn-00afce0c) 範囲 `[['00afce0c', '00afce13']]`
  - `CONDITIONAL_JUMP` [`00afce10`](#insn-00afce10) → [`00afce20`](#insn-00afce20)
  - `FALL_THROUGH` [`00afce10`](#insn-00afce10) → [`00afce14`](#insn-00afce14)
- ブロック [`00afce14`](#insn-00afce14) 範囲 `[['00afce14', '00afce1f']]`
  - `CONDITIONAL_JUMP` [`00afce1c`](#insn-00afce1c) → [`00afce3c`](#insn-00afce3c)
  - `FALL_THROUGH` [`00afce1c`](#insn-00afce1c) → [`00afce20`](#insn-00afce20)
- ブロック [`00afce20`](#insn-00afce20) 範囲 `[['00afce20', '00afce23']]`
  - `FALL_THROUGH` [`00afce20`](#insn-00afce20) → [`00afce24`](#insn-00afce24)
- ブロック [`00afce24`](#insn-00afce24) 範囲 `[['00afce24', '00afce3b']]`
- ブロック [`00afce3c`](#insn-00afce3c) 範囲 `[['00afce3c', '00afce43']]`
  - `UNCONDITIONAL_JUMP` [`00afce40`](#insn-00afce40) → [`00afce24`](#insn-00afce24)

## 命令位置別の参照

- [`00afcdb4`](#insn-00afcdb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcdb8`](#insn-00afcdb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcdc4`](#insn-00afcdc4) → `00c1b998`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00afcdcc`](#insn-00afcdcc) → `010a0d48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E` · 推定型 `undefined8`
- [`00afcdd4`](#insn-00afcdd4) → [`00bddc20`](../00bdd/00bddc20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc20` · 推定シンボル `None` · 推定型 `None`
- [`00afcddc`](#insn-00afcddc) → `00c1b990`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00afcde0`](#insn-00afcde0) → `010a0d50`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E` · 推定型 `undefined8`
- [`00afcde4`](#insn-00afcde4) → [`00afce20`](#insn-00afce20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcdec`](#insn-00afcdec) → [`00afce20`](#insn-00afce20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afce08`](#insn-00afce08) → [`00afcdf4`](#insn-00afcdf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afce10`](#insn-00afce10) → [`00afce20`](#insn-00afce20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afce1c`](#insn-00afce1c) → [`00afce3c`](#insn-00afce3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afce28`](#insn-00afce28) → [`00bddc30`](../00bdd/00bddc30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc30` · 推定シンボル `None` · 推定型 `None`
- [`00afce2c`](#insn-00afce2c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afce40`](#insn-00afce40) → [`00afce24`](#insn-00afce24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afcdb4`](#insn-00afcdb4)

~~~json
{
  "source": "00afcdb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcdb8`](#insn-00afcdb8)

~~~json
{
  "source": "00afcdb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcdc4`](#insn-00afcdc4)

~~~json
{
  "source": "00afcdc4",
  "target": "00c1b998",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b998",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00afcdcc`](#insn-00afcdcc)

~~~json
{
  "source": "00afcdcc",
  "target": "010a0d48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0d48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afcdd4`](#insn-00afcdd4)

~~~json
{
  "source": "00afcdd4",
  "target": "00bddc20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcddc`](#insn-00afcddc)

~~~json
{
  "source": "00afcddc",
  "target": "00c1b990",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b990",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00afcde0`](#insn-00afcde0)

~~~json
{
  "source": "00afcde0",
  "target": "010a0d50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0d50",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afcde4`](#insn-00afcde4)

~~~json
{
  "source": "00afcde4",
  "target": "00afce20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcdec`](#insn-00afcdec)

~~~json
{
  "source": "00afcdec",
  "target": "00afce20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afce08`](#insn-00afce08)

~~~json
{
  "source": "00afce08",
  "target": "00afcdf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afce10`](#insn-00afce10)

~~~json
{
  "source": "00afce10",
  "target": "00afce20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afce1c`](#insn-00afce1c)

~~~json
{
  "source": "00afce1c",
  "target": "00afce3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afce28`](#insn-00afce28)

~~~json
{
  "source": "00afce28",
  "target": "00bddc30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afce2c`](#insn-00afce2c)

~~~json
{
  "source": "00afce2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afce40`](#insn-00afce40)

~~~json
{
  "source": "00afce40",
  "target": "00afce24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
