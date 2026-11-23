# 00adaf4c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00adb014`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb014.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-9304efe6b594ea8bdfa561cd3a872471)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adaf4c",
  "name": "Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementDismissed",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "274cdf9eca79c043f8912d309b0c63bedf7fb9668bb4a3ba88a3a6441bab9075",
  "source_text_sha256": "274cdf9eca79c043f8912d309b0c63bedf7fb9668bb4a3ba88a3a6441bab9075",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adaf4c",
        "00adafdb"
      ],
      [
        "00adb008",
        "00adb00b"
      ]
    ],
    "bytes_sha256": "13ac691b9e1a317172177d228bcda00f84fabd62805ed69915146b30d2146d6a",
    "instruction_count": 37,
    "instruction_bytes": 148,
    "body_bytes": 148,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00566a7c](../00566/00566a7c.md)
- [00adba18](../00adb/00adba18.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1223 bytes

~~~c

void Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementDismissed
               (undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  undefined8 *puVar2;
  long *plVar3;
  byte local_40 [16];
  void *local_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  FUN_00566a7c(local_40,param_1,param_3);
  puVar2 = (undefined8 *)FUN_00adba18(&DAT_0109fe50,local_40);
  if ((puVar2 != &DAT_0109fe58) && (plVar3 = (long *)puVar2[0x12], plVar3 != (long *)0x0)) {
    (**(code **)(*plVar3 + 0x30))(plVar3,local_40);
  }
  if ((local_40[0] & 1) != 0) {
    _ZdlPv(local_30);
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
                    /* try { // try from 00adafd0 to 00bdb00b has its CatchHandler @ 00adafd0
                       catch() { ... } // from try @ 00adafd0 with catch @ 00adafd0
                       catch() { ... } // from try @ 00adb284 with catch @ 00adafd0
                       catch() { ... } // from try @ 00adb664 with catch @ 00adafd0
                       catch() { ... } // from try @ 00adb6c4 with catch @ 00adafd0 */
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
<a id="insn-00adaf4c"></a> `00adaf4c` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00adaf50"></a> `00adaf50` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adaf54"></a> `00adaf54` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adaf58"></a> `00adaf58` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00adaf5c"></a> `00adaf5c` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00adaf60"></a> `00adaf60` | `e1 03 02 aa` | mov x1,x2 | `FALL_THROUGH`
<a id="insn-00adaf64"></a> `00adaf64` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00adaf68"></a> `00adaf68` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adaf6c"></a> `00adaf6c` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00adaf70"></a> `00adaf70` | `c3 2e ea 97` | bl 0x00566a7c | `UNCONDITIONAL_CALL`
<a id="insn-00adaf74"></a> `00adaf74` | `20 2e 00 b0` | adrp x0,0x109f000 | `FALL_THROUGH`
<a id="insn-00adaf78"></a> `00adaf78` | `00 40 39 91` | add x0,x0,#0xe50 | `FALL_THROUGH`
<a id="insn-00adaf7c"></a> `00adaf7c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00adaf80"></a> `00adaf80` | `a6 02 00 94` | bl 0x00adba18 | `UNCONDITIONAL_CALL`
<a id="insn-00adaf84"></a> `00adaf84` | `28 2e 00 b0` | adrp x8,0x109f000 | `FALL_THROUGH`
<a id="insn-00adaf88"></a> `00adaf88` | `08 61 39 91` | add x8,x8,#0xe58 | `FALL_THROUGH`
<a id="insn-00adaf8c"></a> `00adaf8c` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00adaf90"></a> `00adaf90` | `e0 00 00 54` | b.eq 0x00adafac | `CONDITIONAL_JUMP`
<a id="insn-00adaf94"></a> `00adaf94` | `00 48 40 f9` | ldr x0,[x0, #0x90] | `FALL_THROUGH`
<a id="insn-00adaf98"></a> `00adaf98` | `a0 00 00 b4` | cbz x0,0x00adafac | `CONDITIONAL_JUMP`
<a id="insn-00adaf9c"></a> `00adaf9c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00adafa0"></a> `00adafa0` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00adafa4"></a> `00adafa4` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00adafa8"></a> `00adafa8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adafac"></a> `00adafac` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00adafb0"></a> `00adafb0` | `68 00 00 36` | tbz w8,#0x0,0x00adafbc | `CONDITIONAL_JUMP`
<a id="insn-00adafb4"></a> `00adafb4` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adafb8"></a> `00adafb8` | `ea ff 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adafbc"></a> `00adafbc` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00adafc0"></a> `00adafc0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adafc4"></a> `00adafc4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00adafc8"></a> `00adafc8` | `01 02 00 54` | b.ne 0x00adb008 | `CONDITIONAL_JUMP`
<a id="insn-00adafcc"></a> `00adafcc` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adafd0"></a> `00adafd0` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adafd4"></a> `00adafd4` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00adafd8"></a> `00adafd8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00adb008"></a> `00adb008` | `e2 ff 03 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adaf4c`](#insn-00adaf4c) 範囲 `[['00adaf4c', '00adaf93']]`
  - `CONDITIONAL_JUMP` [`00adaf90`](#insn-00adaf90) → [`00adafac`](#insn-00adafac)
  - `FALL_THROUGH` [`00adaf90`](#insn-00adaf90) → [`00adaf94`](#insn-00adaf94)
- ブロック [`00adaf94`](#insn-00adaf94) 範囲 `[['00adaf94', '00adaf9b']]`
  - `CONDITIONAL_JUMP` [`00adaf98`](#insn-00adaf98) → [`00adafac`](#insn-00adafac)
  - `FALL_THROUGH` [`00adaf98`](#insn-00adaf98) → [`00adaf9c`](#insn-00adaf9c)
- ブロック [`00adaf9c`](#insn-00adaf9c) 範囲 `[['00adaf9c', '00adafab']]`
  - `FALL_THROUGH` [`00adafa8`](#insn-00adafa8) → [`00adafac`](#insn-00adafac)
- ブロック [`00adafac`](#insn-00adafac) 範囲 `[['00adafac', '00adafb3']]`
  - `CONDITIONAL_JUMP` [`00adafb0`](#insn-00adafb0) → [`00adafbc`](#insn-00adafbc)
  - `FALL_THROUGH` [`00adafb0`](#insn-00adafb0) → [`00adafb4`](#insn-00adafb4)
- ブロック [`00adafb4`](#insn-00adafb4) 範囲 `[['00adafb4', '00adafbb']]`
  - `FALL_THROUGH` [`00adafb8`](#insn-00adafb8) → [`00adafbc`](#insn-00adafbc)
- ブロック [`00adafbc`](#insn-00adafbc) 範囲 `[['00adafbc', '00adafcb']]`
  - `CONDITIONAL_JUMP` [`00adafc8`](#insn-00adafc8) → [`00adb008`](#insn-00adb008)
  - `FALL_THROUGH` [`00adafc8`](#insn-00adafc8) → [`00adafcc`](#insn-00adafcc)
- ブロック [`00adafcc`](#insn-00adafcc) 範囲 `[['00adafcc', '00adafcf']]`
  - `FALL_THROUGH` [`00adafcc`](#insn-00adafcc) → [`00adafd0`](#insn-00adafd0)
- ブロック [`00adafd0`](#insn-00adafd0) 範囲 `[['00adafd0', '00adafdb']]`
- ブロック [`00adb008`](#insn-00adb008) 範囲 `[['00adb008', '00adb00b']]`

## 命令位置別の参照

- [`00adaf50`](#insn-00adaf50) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaf54`](#insn-00adaf54) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaf68`](#insn-00adaf68) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaf70`](#insn-00adaf70) → [`00566a7c`](../00566/00566a7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566a7c` · 推定シンボル `None` · 推定型 `None`
- [`00adaf78`](#insn-00adaf78) → `0109fe50`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adaf80`](#insn-00adaf80) → [`00adba18`](../00adb/00adba18.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adba18` · 推定シンボル `None` · 推定型 `None`
- [`00adaf90`](#insn-00adaf90) → [`00adafac`](#insn-00adafac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaf98`](#insn-00adaf98) → [`00adafac`](#insn-00adafac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adafac`](#insn-00adafac) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adafb0`](#insn-00adafb0) → [`00adafbc`](#insn-00adafbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adafb4`](#insn-00adafb4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adafb8`](#insn-00adafb8) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adafc0`](#insn-00adafc0) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adafc8`](#insn-00adafc8) → [`00adb008`](#insn-00adb008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adafcc`](#insn-00adafcc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adafd0`](#insn-00adafd0) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb008`](#insn-00adb008) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adaf50`](#insn-00adaf50)

~~~json
{
  "source": "00adaf50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaf54`](#insn-00adaf54)

~~~json
{
  "source": "00adaf54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaf68`](#insn-00adaf68)

~~~json
{
  "source": "00adaf68",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaf70`](#insn-00adaf70)

~~~json
{
  "source": "00adaf70",
  "target": "00566a7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adaf78`](#insn-00adaf78)

~~~json
{
  "source": "00adaf78",
  "target": "0109fe50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe50",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adaf80`](#insn-00adaf80)

~~~json
{
  "source": "00adaf80",
  "target": "00adba18",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adaf90`](#insn-00adaf90)

~~~json
{
  "source": "00adaf90",
  "target": "00adafac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaf98`](#insn-00adaf98)

~~~json
{
  "source": "00adaf98",
  "target": "00adafac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adafac`](#insn-00adafac)

~~~json
{
  "source": "00adafac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adafb0`](#insn-00adafb0)

~~~json
{
  "source": "00adafb0",
  "target": "00adafbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adafb4`](#insn-00adafb4)

~~~json
{
  "source": "00adafb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adafb8`](#insn-00adafb8)

~~~json
{
  "source": "00adafb8",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adafc0`](#insn-00adafc0)

~~~json
{
  "source": "00adafc0",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adafc8`](#insn-00adafc8)

~~~json
{
  "source": "00adafc8",
  "target": "00adb008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adafcc`](#insn-00adafcc)

~~~json
{
  "source": "00adafcc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adafd0`](#insn-00adafd0)

~~~json
{
  "source": "00adafd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb008`](#insn-00adb008)

~~~json
{
  "source": "00adb008",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
