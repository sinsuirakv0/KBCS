# 00afcca8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afcd70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afcd70.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0063.md#compare-00170565906027dac0bdf9bfbf254e6f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afcca8",
  "name": "_ZN8firebase15CleanupNotifier11FindByOwnerEPv",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "945884a133c7c30a4f3a8d6f550d306e6c1e274b7de88ea4dc3a39679bbde19d",
  "source_text_sha256": "945884a133c7c30a4f3a8d6f550d306e6c1e274b7de88ea4dc3a39679bbde19d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afcca8",
        "00afcd37"
      ]
    ],
    "bytes_sha256": "856b1f9b3ee9de3213828d82f2fcd38e875ca2ca981dcf56b72c8b9515bac8bc",
    "instruction_count": 36,
    "instruction_bytes": 144,
    "body_bytes": 144,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bddc90](../00bdd/00bddc90.md)

## 呼び出し先

- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)

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
  
                    /* try { // try from 00afccac to 00bfccb3 has its CatchHandler @ 00aff3cc */
  uVar4 = *(undefined8 *)
           PTR__ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E_00c1b898;
  _ZN8firebase5Mutex7AcquireEv(uVar4);
  if (*(long *)PTR__ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E_00c1b890 != 0) {
                    /* try { // try from 00afccdc to 00bfccf3 has its CatchHandler @ 00aff3c8 */
    plVar1 = (long *)(*(long *)
                       PTR__ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E_00c1b890 + 8)
    ;
    plVar3 = (long *)*plVar1;
    plVar2 = plVar1;
    if (plVar3 != (long *)0x0) {
      do {
                    /* try { // try from 00afccf4 to 00bfcd67 has its CatchHandler @ 00af560c */
        if ((ulong)plVar3[4] >= param_1) {
          plVar2 = plVar3;
        }
        plVar3 = (long *)plVar3[(ulong)plVar3[4] < param_1];
      } while (plVar3 != (long *)0x0);
      if ((plVar2 != plVar1) && ((ulong)plVar2[4] <= param_1)) {
        lVar5 = plVar2[5];
        goto LAB_00afcd18;
      }
    }
  }
  lVar5 = 0;
LAB_00afcd18:
  _ZN8firebase5Mutex7ReleaseEv(uVar4);
  return lVar5;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afcca8"></a> `00afcca8` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afccac"></a> `00afccac` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afccb0"></a> `00afccb0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00afccb4"></a> `00afccb4` | `e8 08 00 f0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00afccb8"></a> `00afccb8` | `08 4d 44 f9` | ldr x8,[x8, #0x898] | `FALL_THROUGH`
<a id="insn-00afccbc"></a> `00afccbc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00afccc0"></a> `00afccc0` | `13 01 40 f9` | ldr x19,[x8] | `FALL_THROUGH`
<a id="insn-00afccc4"></a> `00afccc4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afccc8"></a> `00afccc8` | `96 83 03 94` | bl 0x00bddb20 | `UNCONDITIONAL_CALL`
<a id="insn-00afcccc"></a> `00afcccc` | `e8 08 00 f0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00afccd0"></a> `00afccd0` | `08 49 44 f9` | ldr x8,[x8, #0x890] | `FALL_THROUGH`
<a id="insn-00afccd4"></a> `00afccd4` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00afccd8"></a> `00afccd8` | `e8 01 00 b4` | cbz x8,0x00afcd14 | `CONDITIONAL_JUMP`
<a id="insn-00afccdc"></a> `00afccdc` | `0a 8d 40 f8` | ldr x10,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00afcce0"></a> `00afcce0` | `aa 01 00 b4` | cbz x10,0x00afcd14 | `CONDITIONAL_JUMP`
<a id="insn-00afcce4"></a> `00afcce4` | `e9 03 08 aa` | mov x9,x8 | `FALL_THROUGH`
<a id="insn-00afcce8"></a> `00afcce8` | `4b 11 40 f9` | ldr x11,[x10, #0x20] | `FALL_THROUGH`
<a id="insn-00afccec"></a> `00afccec` | `7f 01 14 eb` | cmp x11,x20 | `FALL_THROUGH`
<a id="insn-00afccf0"></a> `00afccf0` | `eb 27 9f 1a` | cset w11,cc | `FALL_THROUGH`
<a id="insn-00afccf4"></a> `00afccf4` | `29 31 8a 9a` | csel x9,x9,x10,cc | `FALL_THROUGH`
<a id="insn-00afccf8"></a> `00afccf8` | `4a 59 6b f8` | ldr x10,[x10, w11, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00afccfc"></a> `00afccfc` | `6a ff ff b5` | cbnz x10,0x00afcce8 | `CONDITIONAL_JUMP`
<a id="insn-00afcd00"></a> `00afcd00` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00afcd04"></a> `00afcd04` | `80 00 00 54` | b.eq 0x00afcd14 | `CONDITIONAL_JUMP`
<a id="insn-00afcd08"></a> `00afcd08` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00afcd0c"></a> `00afcd0c` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00afcd10"></a> `00afcd10` | `09 01 00 54` | b.ls 0x00afcd30 | `CONDITIONAL_JUMP`
<a id="insn-00afcd14"></a> `00afcd14` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00afcd18"></a> `00afcd18` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afcd1c"></a> `00afcd1c` | `85 83 03 94` | bl 0x00bddb30 | `UNCONDITIONAL_CALL`
<a id="insn-00afcd20"></a> `00afcd20` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcd24"></a> `00afcd24` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afcd28"></a> `00afcd28` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afcd2c"></a> `00afcd2c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afcd30"></a> `00afcd30` | `34 15 40 f9` | ldr x20,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-00afcd34"></a> `00afcd34` | `f9 ff ff 17` | b 0x00afcd18 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00afcca8`](#insn-00afcca8) 範囲 `[['00afcca8', '00afccab']]`
  - `FALL_THROUGH` [`00afcca8`](#insn-00afcca8) → [`00afccac`](#insn-00afccac)
- ブロック [`00afccac`](#insn-00afccac) 範囲 `[['00afccac', '00afccdb']]`
  - `CONDITIONAL_JUMP` [`00afccd8`](#insn-00afccd8) → [`00afcd14`](#insn-00afcd14)
  - `FALL_THROUGH` [`00afccd8`](#insn-00afccd8) → [`00afccdc`](#insn-00afccdc)
- ブロック [`00afccdc`](#insn-00afccdc) 範囲 `[['00afccdc', '00afcce3']]`
  - `CONDITIONAL_JUMP` [`00afcce0`](#insn-00afcce0) → [`00afcd14`](#insn-00afcd14)
  - `FALL_THROUGH` [`00afcce0`](#insn-00afcce0) → [`00afcce4`](#insn-00afcce4)
- ブロック [`00afcce4`](#insn-00afcce4) 範囲 `[['00afcce4', '00afcce7']]`
  - `FALL_THROUGH` [`00afcce4`](#insn-00afcce4) → [`00afcce8`](#insn-00afcce8)
- ブロック [`00afcce8`](#insn-00afcce8) 範囲 `[['00afcce8', '00afccf3']]`
  - `FALL_THROUGH` [`00afccf0`](#insn-00afccf0) → [`00afccf4`](#insn-00afccf4)
- ブロック [`00afccf4`](#insn-00afccf4) 範囲 `[['00afccf4', '00afccff']]`
  - `CONDITIONAL_JUMP` [`00afccfc`](#insn-00afccfc) → [`00afcce8`](#insn-00afcce8)
  - `FALL_THROUGH` [`00afccfc`](#insn-00afccfc) → [`00afcd00`](#insn-00afcd00)
- ブロック [`00afcd00`](#insn-00afcd00) 範囲 `[['00afcd00', '00afcd07']]`
  - `CONDITIONAL_JUMP` [`00afcd04`](#insn-00afcd04) → [`00afcd14`](#insn-00afcd14)
  - `FALL_THROUGH` [`00afcd04`](#insn-00afcd04) → [`00afcd08`](#insn-00afcd08)
- ブロック [`00afcd08`](#insn-00afcd08) 範囲 `[['00afcd08', '00afcd13']]`
  - `CONDITIONAL_JUMP` [`00afcd10`](#insn-00afcd10) → [`00afcd30`](#insn-00afcd30)
  - `FALL_THROUGH` [`00afcd10`](#insn-00afcd10) → [`00afcd14`](#insn-00afcd14)
- ブロック [`00afcd14`](#insn-00afcd14) 範囲 `[['00afcd14', '00afcd17']]`
  - `FALL_THROUGH` [`00afcd14`](#insn-00afcd14) → [`00afcd18`](#insn-00afcd18)
- ブロック [`00afcd18`](#insn-00afcd18) 範囲 `[['00afcd18', '00afcd2f']]`
- ブロック [`00afcd30`](#insn-00afcd30) 範囲 `[['00afcd30', '00afcd37']]`
  - `UNCONDITIONAL_JUMP` [`00afcd34`](#insn-00afcd34) → [`00afcd18`](#insn-00afcd18)

## 命令位置別の参照

- [`00afcca8`](#insn-00afcca8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afccac`](#insn-00afccac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afccb8`](#insn-00afccb8) → `00c1b898`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00afccc0`](#insn-00afccc0) → `010a0c48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E` · 推定型 `undefined8`
- [`00afccc8`](#insn-00afccc8) → [`00bddb20`](../00bdd/00bddb20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb20` · 推定シンボル `None` · 推定型 `None`
- [`00afccd0`](#insn-00afccd0) → `00c1b890`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00afccd4`](#insn-00afccd4) → `010a0c50`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E` · 推定型 `undefined8`
- [`00afccd8`](#insn-00afccd8) → [`00afcd14`](#insn-00afcd14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcce0`](#insn-00afcce0) → [`00afcd14`](#insn-00afcd14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afccfc`](#insn-00afccfc) → [`00afcce8`](#insn-00afcce8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcd04`](#insn-00afcd04) → [`00afcd14`](#insn-00afcd14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcd10`](#insn-00afcd10) → [`00afcd30`](#insn-00afcd30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcd1c`](#insn-00afcd1c) → [`00bddb30`](../00bdd/00bddb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb30` · 推定シンボル `None` · 推定型 `None`
- [`00afcd20`](#insn-00afcd20) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcd34`](#insn-00afcd34) → [`00afcd18`](#insn-00afcd18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afcca8`](#insn-00afcca8)

~~~json
{
  "source": "00afcca8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afccac`](#insn-00afccac)

~~~json
{
  "source": "00afccac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afccb8`](#insn-00afccb8)

~~~json
{
  "source": "00afccb8",
  "target": "00c1b898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b898",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00afccc0`](#insn-00afccc0)

~~~json
{
  "source": "00afccc0",
  "target": "010a0c48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0c48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afccc8`](#insn-00afccc8)

~~~json
{
  "source": "00afccc8",
  "target": "00bddb20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afccd0`](#insn-00afccd0)

~~~json
{
  "source": "00afccd0",
  "target": "00c1b890",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b890",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00afccd4`](#insn-00afccd4)

~~~json
{
  "source": "00afccd4",
  "target": "010a0c50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0c50",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afccd8`](#insn-00afccd8)

~~~json
{
  "source": "00afccd8",
  "target": "00afcd14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcce0`](#insn-00afcce0)

~~~json
{
  "source": "00afcce0",
  "target": "00afcd14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afccfc`](#insn-00afccfc)

~~~json
{
  "source": "00afccfc",
  "target": "00afcce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcd04`](#insn-00afcd04)

~~~json
{
  "source": "00afcd04",
  "target": "00afcd14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcd10`](#insn-00afcd10)

~~~json
{
  "source": "00afcd10",
  "target": "00afcd30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcd1c`](#insn-00afcd1c)

~~~json
{
  "source": "00afcd1c",
  "target": "00bddb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcd20`](#insn-00afcd20)

~~~json
{
  "source": "00afcd20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcd34`](#insn-00afcd34)

~~~json
{
  "source": "00afcd34",
  "target": "00afcd18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
