# 004ababc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `004ababc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ab/004ababc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0009.md#compare-f71fb0d538962db7d9540ae4df11bdc6)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004ababc",
  "name": "_ZNK5Botan3MD510copy_stateEv",
  "size": 176,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3846937d79ea3d3b9b281b38d100bba070a72f61f9872514274427c1c1388c8d",
  "source_text_sha256": "3846937d79ea3d3b9b281b38d100bba070a72f61f9872514274427c1c1388c8d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004ababc",
        "004abb6b"
      ]
    ],
    "bytes_sha256": "495285252e4ea89b77c6bdac9f77d74b7daf06d3f9a9daa7d0e2e461d9568da5",
    "instruction_count": 44,
    "instruction_bytes": 176,
    "body_bytes": 176,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [005132d4](../00513/005132d4.md)
- [0051d3cc](../0051d/0051d3cc.md)
- [00bdaf40](../00bda/00bdaf40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 991 bytes

~~~c

void _ZNK5Botan3MD510copy_stateEv(undefined8 *param_1,long param_2)

{
  long lVar1;
  long lVar2;
  undefined *puVar3;
  long *plVar4;
  long lVar5;
  long lVar6;
  long lVar7;
  long lVar8;
  
  plVar4 = (long *)_Znwm(0x70);
  puVar3 = PTR__ZTVN5Botan16MDx_HashFunctionE_00c1b048;
  plVar4[2] = 0;
  plVar4[3] = 0;
  *plVar4 = (long)(puVar3 + 0x10);
  plVar4[1] = 0;
  FUN_0051d3cc();
  puVar3 = PTR__ZTVN5Botan3MD5E_00c1b068;
  lVar6 = *(long *)(param_2 + 0x28);
  lVar5 = *(long *)(param_2 + 0x20);
  lVar8 = *(long *)(param_2 + 0x38);
  lVar7 = *(long *)(param_2 + 0x30);
  lVar1 = *(long *)(param_2 + 0x40);
  lVar2 = *(long *)(param_2 + 0x48);
  plVar4[9] = 0;
  plVar4[10] = 0;
  plVar4[5] = lVar6;
  plVar4[4] = lVar5;
  plVar4[7] = lVar8;
  plVar4[6] = lVar7;
  *plVar4 = (long)(puVar3 + 0x10);
  plVar4[8] = 0;
  FUN_005132d4(plVar4 + 8,lVar1,lVar2,lVar2 - lVar1 >> 2);
  plVar4[0xb] = 0;
  plVar4[0xc] = 0;
  plVar4[0xd] = 0;
  FUN_005132d4();
  *param_1 = plVar4;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004ababc"></a> `004ababc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-004abac0"></a> `004abac0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004abac4"></a> `004abac4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004abac8"></a> `004abac8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-004abacc"></a> `004abacc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-004abad0"></a> `004abad0` | `00 0e 80 52` | mov w0,#0x70 | `FALL_THROUGH`
<a id="insn-004abad4"></a> `004abad4` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-004abad8"></a> `004abad8` | `1a bd 1c 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-004abadc"></a> `004abadc` | `88 3b 00 90` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-004abae0"></a> `004abae0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004abae4"></a> `004abae4` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-004abae8"></a> `004abae8` | `a1 8a 40 a9` | ldp x1,x2,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-004abaec"></a> `004abaec` | `1f 7c 01 a9` | stp xzr,xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004abaf0"></a> `004abaf0` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-004abaf4"></a> `004abaf4` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-004abaf8"></a> `004abaf8` | `43 00 01 cb` | sub x3,x2,x1 | `FALL_THROUGH`
<a id="insn-004abafc"></a> `004abafc` | `1f 8c 00 f8` | str xzr,[x0, #0x8]! | `FALL_THROUGH`
<a id="insn-004abb00"></a> `004abb00` | `33 c6 01 94` | bl 0x0051d3cc | `UNCONDITIONAL_CALL`
<a id="insn-004abb04"></a> `004abb04` | `88 3b 00 90` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-004abb08"></a> `004abb08` | `a0 06 41 ad` | ldp q0,q1,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-004abb0c"></a> `004abb0c` | `08 35 40 f9` | ldr x8,[x8, #0x68] | `FALL_THROUGH`
<a id="insn-004abb10"></a> `004abb10` | `a1 0a 44 a9` | ldp x1,x2,[x21, #0x40] | `FALL_THROUGH`
<a id="insn-004abb14"></a> `004abb14` | `f6 03 13 aa` | mov x22,x19 | `FALL_THROUGH`
<a id="insn-004abb18"></a> `004abb18` | `7f fe 04 a9` | stp xzr,xzr,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-004abb1c"></a> `004abb1c` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-004abb20"></a> `004abb20` | `60 06 01 ad` | stp q0,q1,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-004abb24"></a> `004abb24` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-004abb28"></a> `004abb28` | `48 00 01 cb` | sub x8,x2,x1 | `FALL_THROUGH`
<a id="insn-004abb2c"></a> `004abb2c` | `df 0e 04 f8` | str xzr,[x22, #0x40]! | `FALL_THROUGH`
<a id="insn-004abb30"></a> `004abb30` | `03 fd 42 93` | asr x3,x8,#0x2 | `FALL_THROUGH`
<a id="insn-004abb34"></a> `004abb34` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-004abb38"></a> `004abb38` | `e7 9d 01 94` | bl 0x005132d4 | `UNCONDITIONAL_CALL`
<a id="insn-004abb3c"></a> `004abb3c` | `a1 8a 45 a9` | ldp x1,x2,[x21, #0x58] | `FALL_THROUGH`
<a id="insn-004abb40"></a> `004abb40` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004abb44"></a> `004abb44` | `1f fc 85 a9` | stp xzr,xzr,[x0, #0x58]! | `FALL_THROUGH`
<a id="insn-004abb48"></a> `004abb48` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004abb4c"></a> `004abb4c` | `48 00 01 cb` | sub x8,x2,x1 | `FALL_THROUGH`
<a id="insn-004abb50"></a> `004abb50` | `03 fd 42 93` | asr x3,x8,#0x2 | `FALL_THROUGH`
<a id="insn-004abb54"></a> `004abb54` | `e0 9d 01 94` | bl 0x005132d4 | `UNCONDITIONAL_CALL`
<a id="insn-004abb58"></a> `004abb58` | `93 02 00 f9` | str x19,[x20] | `FALL_THROUGH`
<a id="insn-004abb5c"></a> `004abb5c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004abb60"></a> `004abb60` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004abb64"></a> `004abb64` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-004abb68"></a> `004abb68` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004ababc`](#insn-004ababc) 範囲 `[['004ababc', '004abb6b']]`

## 命令位置別の参照

- [`004ababc`](#insn-004ababc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abac0`](#insn-004abac0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abac4`](#insn-004abac4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abad8`](#insn-004abad8) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`004abae4`](#insn-004abae4) → `00c1b048`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004abaf4`](#insn-004abaf4) → `00be9c18`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`004abb00`](#insn-004abb00) → [`0051d3cc`](../0051d/0051d3cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0051d3cc` · 推定シンボル `None` · 推定型 `None`
- [`004abb0c`](#insn-004abb0c) → `00c1b068`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004abb24`](#insn-004abb24) → `00beb3a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`004abb38`](#insn-004abb38) → [`005132d4`](../00513/005132d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005132d4` · 推定シンボル `None` · 推定型 `None`
- [`004abb54`](#insn-004abb54) → [`005132d4`](../00513/005132d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005132d4` · 推定シンボル `None` · 推定型 `None`
- [`004abb5c`](#insn-004abb5c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abb60`](#insn-004abb60) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abb64`](#insn-004abb64) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004ababc`](#insn-004ababc)

~~~json
{
  "source": "004ababc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abac0`](#insn-004abac0)

~~~json
{
  "source": "004abac0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abac4`](#insn-004abac4)

~~~json
{
  "source": "004abac4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abad8`](#insn-004abad8)

~~~json
{
  "source": "004abad8",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004abae4`](#insn-004abae4)

~~~json
{
  "source": "004abae4",
  "target": "00c1b048",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b048",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004abaf4`](#insn-004abaf4)

~~~json
{
  "source": "004abaf4",
  "target": "00be9c18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be9c08",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004abb00`](#insn-004abb00)

~~~json
{
  "source": "004abb00",
  "target": "0051d3cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004abb0c`](#insn-004abb0c)

~~~json
{
  "source": "004abb0c",
  "target": "00c1b068",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b068",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004abb24`](#insn-004abb24)

~~~json
{
  "source": "004abb24",
  "target": "00beb3a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00beb398",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004abb38`](#insn-004abb38)

~~~json
{
  "source": "004abb38",
  "target": "005132d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004abb54`](#insn-004abb54)

~~~json
{
  "source": "004abb54",
  "target": "005132d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004abb5c`](#insn-004abb5c)

~~~json
{
  "source": "004abb5c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abb60`](#insn-004abb60)

~~~json
{
  "source": "004abb60",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abb64`](#insn-004abb64)

~~~json
{
  "source": "004abb64",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
