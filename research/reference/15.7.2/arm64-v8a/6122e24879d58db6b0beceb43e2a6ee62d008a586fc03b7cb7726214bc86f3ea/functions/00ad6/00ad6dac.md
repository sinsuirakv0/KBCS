# 00ad6dac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ad6e74`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6e74.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-aaea4d0c154fe5ff886662740a9db506)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ad6dac",
  "name": "Java_jp_co_ponos_battlecats_MyGoogleSignInListener_onFailure",
  "size": 172,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "500c39f25ba4290cf55a1fa82c88b6e3012ddffc800e08617bef2b162bda850c",
  "source_text_sha256": "500c39f25ba4290cf55a1fa82c88b6e3012ddffc800e08617bef2b162bda850c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ad6dac",
        "00ad6e53"
      ],
      [
        "00ad6e80",
        "00ad6e83"
      ]
    ],
    "bytes_sha256": "0bcfad06530beff21536ab5b73d9341c8fef6d1ffeba52ed4f6ccb57db0f21a8",
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

- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 関連文字列（未確認候補）

~~~text
"Google サインイン 失敗"
"ンイン 失敗"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1254 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void Java_jp_co_ponos_battlecats_MyGoogleSignInListener_onFailure(void)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  long *plVar6;
  ulong local_50;
  undefined8 uStack_48;
  undefined8 *local_40;
  undefined4 local_2c;
  long local_28;
  
  plVar6 = DAT_0109fcc0;
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  if (DAT_0109fcc0 != (long *)0x0) {
    local_40 = (undefined8 *)_Znwm(0x20);
    uStack_48 = _UNK_002b14c8;
    local_50 = _DAT_002b14c0;
    uVar5 = _UNK_002a7d29;
    uVar4 = _DAT_002a7d14;
    uVar2 = CONCAT35(_DAT_002a7d21,_UNK_002a7d1c);
    uVar3 = CONCAT53(_UNK_002a7d24,_DAT_002a7d21);
    *(undefined1 *)((long)local_40 + 0x1d) = 0;
    local_40[1] = uVar2;
    *local_40 = uVar4;
    *(undefined8 *)((long)local_40 + 0x15) = uVar5;
    *(undefined8 *)((long)local_40 + 0xd) = uVar3;
    local_2c = 0;
    (**(code **)(*plVar6 + 0x30))(plVar6,&local_2c,&local_50);
    if ((local_50 & 1) != 0) {
      _ZdlPv(local_40);
    }
  }
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
<a id="insn-00ad6dac"></a> `00ad6dac` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00ad6db0"></a> `00ad6db0` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ad6db4"></a> `00ad6db4` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ad6db8"></a> `00ad6db8` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00ad6dbc"></a> `00ad6dbc` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00ad6dc0"></a> `00ad6dc0` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00ad6dc4"></a> `00ad6dc4` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad6dc8"></a> `00ad6dc8` | `48 2e 00 b0` | adrp x8,0x109f000 | `FALL_THROUGH`
<a id="insn-00ad6dcc"></a> `00ad6dcc` | `13 61 46 f9` | ldr x19,[x8, #0xcc0] | `FALL_THROUGH`
<a id="insn-00ad6dd0"></a> `00ad6dd0` | `33 03 00 b4` | cbz x19,0x00ad6e34 | `CONDITIONAL_JUMP`
<a id="insn-00ad6dd4"></a> `00ad6dd4` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00ad6dd8"></a> `00ad6dd8` | `5a 10 04 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00ad6ddc"></a> `00ad6ddc` | `c8 be ff f0` | adrp x8,0x2b1000 | `FALL_THROUGH`
<a id="insn-00ad6de0"></a> `00ad6de0` | `89 be ff b0` | adrp x9,0x2a7000 | `FALL_THROUGH`
<a id="insn-00ad6de4"></a> `00ad6de4` | `29 51 34 91` | add x9,x9,#0xd14 | `FALL_THROUGH`
<a id="insn-00ad6de8"></a> `00ad6de8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00ad6dec"></a> `00ad6dec` | `01 31 c1 3d` | ldr q1,[x8, #0x4c0] | `FALL_THROUGH`
<a id="insn-00ad6df0"></a> `00ad6df0` | `22 d1 c0 3c` | ldur q2,[x9, #0xd] | `FALL_THROUGH`
<a id="insn-00ad6df4"></a> `00ad6df4` | `1f 74 00 39` | strb wzr,[x0, #0x1d] | `FALL_THROUGH`
<a id="insn-00ad6df8"></a> `00ad6df8` | `00 00 80 3d` | str q0,[x0] | `FALL_THROUGH`
<a id="insn-00ad6dfc"></a> `00ad6dfc` | `e1 03 80 3d` | str q1,[sp] | `FALL_THROUGH`
<a id="insn-00ad6e00"></a> `00ad6e00` | `02 d0 80 3c` | stur q2,[x0, #0xd] | `FALL_THROUGH`
<a id="insn-00ad6e04"></a> `00ad6e04` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ad6e08"></a> `00ad6e08` | `e0 0b 00 f9` | str x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ad6e0c"></a> `00ad6e0c` | `bf 43 1f b8` | stur wzr,[x29, #-0xc] | `FALL_THROUGH`
<a id="insn-00ad6e10"></a> `00ad6e10` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00ad6e14"></a> `00ad6e14` | `a1 33 00 d1` | sub x1,x29,#0xc | `FALL_THROUGH`
<a id="insn-00ad6e18"></a> `00ad6e18` | `e2 03 00 91` | mov x2,sp | `FALL_THROUGH`
<a id="insn-00ad6e1c"></a> `00ad6e1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ad6e20"></a> `00ad6e20` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad6e24"></a> `00ad6e24` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00ad6e28"></a> `00ad6e28` | `68 00 00 36` | tbz w8,#0x0,0x00ad6e34 | `CONDITIONAL_JUMP`
<a id="insn-00ad6e2c"></a> `00ad6e2c` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ad6e30"></a> `00ad6e30` | `4c 10 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00ad6e34"></a> `00ad6e34` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00ad6e38"></a> `00ad6e38` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad6e3c"></a> `00ad6e3c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ad6e40"></a> `00ad6e40` | `01 02 00 54` | b.ne 0x00ad6e80 | `CONDITIONAL_JUMP`
<a id="insn-00ad6e44"></a> `00ad6e44` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ad6e48"></a> `00ad6e48` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ad6e4c"></a> `00ad6e4c` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00ad6e50"></a> `00ad6e50` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ad6e80"></a> `00ad6e80` | `44 10 04 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ad6dac`](#insn-00ad6dac) 範囲 `[['00ad6dac', '00ad6dd3']]`
  - `CONDITIONAL_JUMP` [`00ad6dd0`](#insn-00ad6dd0) → [`00ad6e34`](#insn-00ad6e34)
  - `FALL_THROUGH` [`00ad6dd0`](#insn-00ad6dd0) → [`00ad6dd4`](#insn-00ad6dd4)
- ブロック [`00ad6dd4`](#insn-00ad6dd4) 範囲 `[['00ad6dd4', '00ad6e2b']]`
  - `CONDITIONAL_JUMP` [`00ad6e28`](#insn-00ad6e28) → [`00ad6e34`](#insn-00ad6e34)
  - `FALL_THROUGH` [`00ad6e28`](#insn-00ad6e28) → [`00ad6e2c`](#insn-00ad6e2c)
- ブロック [`00ad6e2c`](#insn-00ad6e2c) 範囲 `[['00ad6e2c', '00ad6e33']]`
  - `FALL_THROUGH` [`00ad6e30`](#insn-00ad6e30) → [`00ad6e34`](#insn-00ad6e34)
- ブロック [`00ad6e34`](#insn-00ad6e34) 範囲 `[['00ad6e34', '00ad6e43']]`
  - `CONDITIONAL_JUMP` [`00ad6e40`](#insn-00ad6e40) → [`00ad6e80`](#insn-00ad6e80)
  - `FALL_THROUGH` [`00ad6e40`](#insn-00ad6e40) → [`00ad6e44`](#insn-00ad6e44)
- ブロック [`00ad6e44`](#insn-00ad6e44) 範囲 `[['00ad6e44', '00ad6e53']]`
- ブロック [`00ad6e80`](#insn-00ad6e80) 範囲 `[['00ad6e80', '00ad6e83']]`

## 命令位置別の参照

- [`00ad6db0`](#insn-00ad6db0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6db4`](#insn-00ad6db4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6dc4`](#insn-00ad6dc4) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6dcc`](#insn-00ad6dcc) → `0109fcc0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad6dd0`](#insn-00ad6dd0) → [`00ad6e34`](#insn-00ad6e34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6dd8`](#insn-00ad6dd8) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00ad6de8`](#insn-00ad6de8) → `002a7d14`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6dec`](#insn-00ad6dec) → `002b14c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6df0`](#insn-00ad6df0) → `002a7d21`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6dfc`](#insn-00ad6dfc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6e08`](#insn-00ad6e08) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6e0c`](#insn-00ad6e0c) → `Stack[-0x2c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6e24`](#insn-00ad6e24) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6e28`](#insn-00ad6e28) → [`00ad6e34`](#insn-00ad6e34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6e2c`](#insn-00ad6e2c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6e30`](#insn-00ad6e30) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00ad6e38`](#insn-00ad6e38) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6e40`](#insn-00ad6e40) → [`00ad6e80`](#insn-00ad6e80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6e44`](#insn-00ad6e44) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6e48`](#insn-00ad6e48) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6e80`](#insn-00ad6e80) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ad6db0`](#insn-00ad6db0)

~~~json
{
  "source": "00ad6db0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6db4`](#insn-00ad6db4)

~~~json
{
  "source": "00ad6db4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6dc4`](#insn-00ad6dc4)

~~~json
{
  "source": "00ad6dc4",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6dcc`](#insn-00ad6dcc)

~~~json
{
  "source": "00ad6dcc",
  "target": "0109fcc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fcc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad6dd0`](#insn-00ad6dd0)

~~~json
{
  "source": "00ad6dd0",
  "target": "00ad6e34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6dd8`](#insn-00ad6dd8)

~~~json
{
  "source": "00ad6dd8",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad6de8`](#insn-00ad6de8)

~~~json
{
  "source": "00ad6de8",
  "target": "002a7d14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6dec`](#insn-00ad6dec)

~~~json
{
  "source": "00ad6dec",
  "target": "002b14c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6df0`](#insn-00ad6df0)

~~~json
{
  "source": "00ad6df0",
  "target": "002a7d21",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6dfc`](#insn-00ad6dfc)

~~~json
{
  "source": "00ad6dfc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6e08`](#insn-00ad6e08)

~~~json
{
  "source": "00ad6e08",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6e0c`](#insn-00ad6e0c)

~~~json
{
  "source": "00ad6e0c",
  "target": "Stack[-0x2c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6e24`](#insn-00ad6e24)

~~~json
{
  "source": "00ad6e24",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6e28`](#insn-00ad6e28)

~~~json
{
  "source": "00ad6e28",
  "target": "00ad6e34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6e2c`](#insn-00ad6e2c)

~~~json
{
  "source": "00ad6e2c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6e30`](#insn-00ad6e30)

~~~json
{
  "source": "00ad6e30",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad6e38`](#insn-00ad6e38)

~~~json
{
  "source": "00ad6e38",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6e40`](#insn-00ad6e40)

~~~json
{
  "source": "00ad6e40",
  "target": "00ad6e80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6e44`](#insn-00ad6e44)

~~~json
{
  "source": "00ad6e44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6e48`](#insn-00ad6e48)

~~~json
{
  "source": "00ad6e48",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6e80`](#insn-00ad6e80)

~~~json
{
  "source": "00ad6e80",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
