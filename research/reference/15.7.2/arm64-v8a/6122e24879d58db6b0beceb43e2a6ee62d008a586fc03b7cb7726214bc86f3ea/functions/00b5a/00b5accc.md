# 00b5accc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b5ad94`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5ad94.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0068.md#compare-b1363f5f71d95dd0dbb4f9a6283faa4e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5accc",
  "name": "_ZN8firebase4auth4Auth8FindAuthEPNS_3AppE",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "359950d82669be1a9c810298ac2454fecbcfa4871bc6cda80d3ddc82f917868f",
  "source_text_sha256": "359950d82669be1a9c810298ac2454fecbcfa4871bc6cda80d3ddc82f917868f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5accc",
        "00b5ad57"
      ]
    ],
    "bytes_sha256": "fb2cf79d278af9981a7810e3f9a8df028f1a103699a31fdd04d1307dc80fa07c",
    "instruction_count": 35,
    "instruction_bytes": 140,
    "body_bytes": 140,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1234 bytes

~~~c

undefined8 _ZN8firebase4auth4Auth8FindAuthEPNS_3AppE(ulong param_1)

{
  undefined *puVar1;
  undefined *puVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  
  uVar3 = *(undefined8 *)PTR__ZN8firebase4auth13g_auths_mutexE_00c1ba70;
                    /* try { // try from 00b5acec to 00c5acff has its CatchHandler @ 00b5ae88 */
  _ZN8firebase5Mutex7AcquireEv(uVar3);
  puVar2 = *(undefined **)(PTR__ZN8firebase4auth7g_authsE_00c1ba78 + 8);
  if (puVar2 != (undefined *)0x0) {
    puVar1 = PTR__ZN8firebase4auth7g_authsE_00c1ba78 + 8;
    do {
      if (*(ulong *)(puVar2 + 0x20) >= param_1) {
        puVar1 = puVar2;
      }
      puVar2 = *(undefined **)(puVar2 + (ulong)(*(ulong *)(puVar2 + 0x20) < param_1) * 8);
    } while (puVar2 != (undefined *)0x0);
    if ((puVar1 != PTR__ZN8firebase4auth7g_authsE_00c1ba78 + 8) &&
       (*(ulong *)(puVar1 + 0x20) <= param_1)) {
      uVar4 = *(undefined8 *)(puVar1 + 0x28);
      goto LAB_00b5ad38;
    }
  }
                    /* try { // try from 00b5ad34 to 00c5ad43 has its CatchHandler @ 00b5aea4 */
  uVar4 = 0;
LAB_00b5ad38:
  _ZN8firebase5Mutex7ReleaseEv(uVar3);
                    /* try { // try from 00b5ad44 to 00c5ad57 has its CatchHandler @ 00b5ae8c */
  return uVar4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b5accc"></a> `00b5accc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b5acd0"></a> `00b5acd0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5acd4"></a> `00b5acd4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b5acd8"></a> `00b5acd8` | `08 06 00 b0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00b5acdc"></a> `00b5acdc` | `08 39 45 f9` | ldr x8,[x8, #0xa70] | `FALL_THROUGH`
<a id="insn-00b5ace0"></a> `00b5ace0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b5ace4"></a> `00b5ace4` | `13 01 40 f9` | ldr x19,[x8] | `FALL_THROUGH`
<a id="insn-00b5ace8"></a> `00b5ace8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5acec"></a> `00b5acec` | `8d 0b 02 94` | bl 0x00bddb20 | `UNCONDITIONAL_CALL`
<a id="insn-00b5acf0"></a> `00b5acf0` | `09 06 00 b0` | adrp x9,0xc1b000 | `FALL_THROUGH`
<a id="insn-00b5acf4"></a> `00b5acf4` | `29 3d 45 f9` | ldr x9,[x9, #0xa78] | `FALL_THROUGH`
<a id="insn-00b5acf8"></a> `00b5acf8` | `2a 05 40 f9` | ldr x10,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00b5acfc"></a> `00b5acfc` | `ca 01 00 b4` | cbz x10,0x00b5ad34 | `CONDITIONAL_JUMP`
<a id="insn-00b5ad00"></a> `00b5ad00` | `28 21 00 91` | add x8,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00b5ad04"></a> `00b5ad04` | `4b 11 40 f9` | ldr x11,[x10, #0x20] | `FALL_THROUGH`
<a id="insn-00b5ad08"></a> `00b5ad08` | `7f 01 14 eb` | cmp x11,x20 | `FALL_THROUGH`
<a id="insn-00b5ad0c"></a> `00b5ad0c` | `eb 27 9f 1a` | cset w11,cc | `FALL_THROUGH`
<a id="insn-00b5ad10"></a> `00b5ad10` | `08 31 8a 9a` | csel x8,x8,x10,cc | `FALL_THROUGH`
<a id="insn-00b5ad14"></a> `00b5ad14` | `4a 59 6b f8` | ldr x10,[x10, w11, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00b5ad18"></a> `00b5ad18` | `6a ff ff b5` | cbnz x10,0x00b5ad04 | `CONDITIONAL_JUMP`
<a id="insn-00b5ad1c"></a> `00b5ad1c` | `29 21 00 91` | add x9,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00b5ad20"></a> `00b5ad20` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b5ad24"></a> `00b5ad24` | `80 00 00 54` | b.eq 0x00b5ad34 | `CONDITIONAL_JUMP`
<a id="insn-00b5ad28"></a> `00b5ad28` | `09 11 40 f9` | ldr x9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00b5ad2c"></a> `00b5ad2c` | `3f 01 14 eb` | cmp x9,x20 | `FALL_THROUGH`
<a id="insn-00b5ad30"></a> `00b5ad30` | `09 01 00 54` | b.ls 0x00b5ad50 | `CONDITIONAL_JUMP`
<a id="insn-00b5ad34"></a> `00b5ad34` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00b5ad38"></a> `00b5ad38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5ad3c"></a> `00b5ad3c` | `7d 0b 02 94` | bl 0x00bddb30 | `UNCONDITIONAL_CALL`
<a id="insn-00b5ad40"></a> `00b5ad40` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5ad44"></a> `00b5ad44` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b5ad48"></a> `00b5ad48` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b5ad4c"></a> `00b5ad4c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b5ad50"></a> `00b5ad50` | `14 15 40 f9` | ldr x20,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00b5ad54"></a> `00b5ad54` | `f9 ff ff 17` | b 0x00b5ad38 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00b5accc`](#insn-00b5accc) 範囲 `[['00b5accc', '00b5aceb']]`
  - `FALL_THROUGH` [`00b5ace8`](#insn-00b5ace8) → [`00b5acec`](#insn-00b5acec)
- ブロック [`00b5acec`](#insn-00b5acec) 範囲 `[['00b5acec', '00b5acff']]`
  - `CONDITIONAL_JUMP` [`00b5acfc`](#insn-00b5acfc) → [`00b5ad34`](#insn-00b5ad34)
  - `FALL_THROUGH` [`00b5acfc`](#insn-00b5acfc) → [`00b5ad00`](#insn-00b5ad00)
- ブロック [`00b5ad00`](#insn-00b5ad00) 範囲 `[['00b5ad00', '00b5ad03']]`
  - `FALL_THROUGH` [`00b5ad00`](#insn-00b5ad00) → [`00b5ad04`](#insn-00b5ad04)
- ブロック [`00b5ad04`](#insn-00b5ad04) 範囲 `[['00b5ad04', '00b5ad1b']]`
  - `CONDITIONAL_JUMP` [`00b5ad18`](#insn-00b5ad18) → [`00b5ad04`](#insn-00b5ad04)
  - `FALL_THROUGH` [`00b5ad18`](#insn-00b5ad18) → [`00b5ad1c`](#insn-00b5ad1c)
- ブロック [`00b5ad1c`](#insn-00b5ad1c) 範囲 `[['00b5ad1c', '00b5ad27']]`
  - `CONDITIONAL_JUMP` [`00b5ad24`](#insn-00b5ad24) → [`00b5ad34`](#insn-00b5ad34)
  - `FALL_THROUGH` [`00b5ad24`](#insn-00b5ad24) → [`00b5ad28`](#insn-00b5ad28)
- ブロック [`00b5ad28`](#insn-00b5ad28) 範囲 `[['00b5ad28', '00b5ad33']]`
  - `CONDITIONAL_JUMP` [`00b5ad30`](#insn-00b5ad30) → [`00b5ad50`](#insn-00b5ad50)
  - `FALL_THROUGH` [`00b5ad30`](#insn-00b5ad30) → [`00b5ad34`](#insn-00b5ad34)
- ブロック [`00b5ad34`](#insn-00b5ad34) 範囲 `[['00b5ad34', '00b5ad37']]`
  - `FALL_THROUGH` [`00b5ad34`](#insn-00b5ad34) → [`00b5ad38`](#insn-00b5ad38)
- ブロック [`00b5ad38`](#insn-00b5ad38) 範囲 `[['00b5ad38', '00b5ad43']]`
  - `FALL_THROUGH` [`00b5ad40`](#insn-00b5ad40) → [`00b5ad44`](#insn-00b5ad44)
- ブロック [`00b5ad44`](#insn-00b5ad44) 範囲 `[['00b5ad44', '00b5ad4f']]`
- ブロック [`00b5ad50`](#insn-00b5ad50) 範囲 `[['00b5ad50', '00b5ad57']]`
  - `UNCONDITIONAL_JUMP` [`00b5ad54`](#insn-00b5ad54) → [`00b5ad38`](#insn-00b5ad38)

## 命令位置別の参照

- [`00b5accc`](#insn-00b5accc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5acd0`](#insn-00b5acd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5acdc`](#insn-00b5acdc) → `00c1ba70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b5ace4`](#insn-00b5ace4) → `010a1318`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase4auth13g_auths_mutexE` · 推定型 `undefined8`
- [`00b5acec`](#insn-00b5acec) → [`00bddb20`](../00bdd/00bddb20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb20` · 推定シンボル `None` · 推定型 `None`
- [`00b5acf4`](#insn-00b5acf4) → `00c1ba78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b5acf8`](#insn-00b5acf8) → `010a1308`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b5acfc`](#insn-00b5acfc) → [`00b5ad34`](#insn-00b5ad34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ad18`](#insn-00b5ad18) → [`00b5ad04`](#insn-00b5ad04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ad24`](#insn-00b5ad24) → [`00b5ad34`](#insn-00b5ad34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ad30`](#insn-00b5ad30) → [`00b5ad50`](#insn-00b5ad50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ad3c`](#insn-00b5ad3c) → [`00bddb30`](../00bdd/00bddb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb30` · 推定シンボル `None` · 推定型 `None`
- [`00b5ad40`](#insn-00b5ad40) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ad54`](#insn-00b5ad54) → [`00b5ad38`](#insn-00b5ad38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5accc`](#insn-00b5accc)

~~~json
{
  "source": "00b5accc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5acd0`](#insn-00b5acd0)

~~~json
{
  "source": "00b5acd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5acdc`](#insn-00b5acdc)

~~~json
{
  "source": "00b5acdc",
  "target": "00c1ba70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ba70",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b5ace4`](#insn-00b5ace4)

~~~json
{
  "source": "00b5ace4",
  "target": "010a1318",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1318",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5acec`](#insn-00b5acec)

~~~json
{
  "source": "00b5acec",
  "target": "00bddb20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5acf4`](#insn-00b5acf4)

~~~json
{
  "source": "00b5acf4",
  "target": "00c1ba78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ba78",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b5acf8`](#insn-00b5acf8)

~~~json
{
  "source": "00b5acf8",
  "target": "010a1308",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1308",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5acfc`](#insn-00b5acfc)

~~~json
{
  "source": "00b5acfc",
  "target": "00b5ad34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ad18`](#insn-00b5ad18)

~~~json
{
  "source": "00b5ad18",
  "target": "00b5ad04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ad24`](#insn-00b5ad24)

~~~json
{
  "source": "00b5ad24",
  "target": "00b5ad34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ad30`](#insn-00b5ad30)

~~~json
{
  "source": "00b5ad30",
  "target": "00b5ad50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ad3c`](#insn-00b5ad3c)

~~~json
{
  "source": "00b5ad3c",
  "target": "00bddb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5ad40`](#insn-00b5ad40)

~~~json
{
  "source": "00b5ad40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ad54`](#insn-00b5ad54)

~~~json
{
  "source": "00b5ad54",
  "target": "00b5ad38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
