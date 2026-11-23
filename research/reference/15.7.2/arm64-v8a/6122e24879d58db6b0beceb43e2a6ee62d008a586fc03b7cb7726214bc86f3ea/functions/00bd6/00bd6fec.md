# 00bd6fec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bd70ac`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) · 移動量 `+0xc0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0080.md#compare-463b6eeaed76906e66a84c5459d19eaa)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd6fec",
  "name": "FUN_00bd6fec",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1f80d7a65073dbdc148e56626a701183d6fa0e8d40bf9bfe5225922cca0ee29c",
  "source_text_sha256": "1f80d7a65073dbdc148e56626a701183d6fa0e8d40bf9bfe5225922cca0ee29c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd6fec",
        "00bd706f"
      ]
    ],
    "bytes_sha256": "8c2e49cccf2be009d72fa1a854a36cacb3de7ba50750ccd7213e00e00273aff4",
    "instruction_count": 33,
    "instruction_bytes": 132,
    "body_bytes": 132,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0043e5d8](../0043e/0043e5d8.md)
- [0043e940](../0043e/0043e940.md)
- [00445124](../00445/00445124.md)
- [00450668](../00450/00450668.md)
- [00455270](../00455/00455270.md)
- [00458634](../00458/00458634.md)
- [00478d84](../00478/00478d84.md)
- [0047ba2c](../0047b/0047ba2c.md)
- [0047bdcc](../0047b/0047bdcc.md)
- [00482154](../00482/00482154.md)
- [00484e1c](../00484/00484e1c.md)
- [0049bfc8](../0049b/0049bfc8.md)
- [004e01ec](../004e0/004e01ec.md)
- [004e5d50](../004e5/004e5d50.md)
- [004ec514](../004ec/004ec514.md)
- [004ede80](../004ed/004ede80.md)
- [004ee34c](../004ee/004ee34c.md)
- [004ee4f4](../004ee/004ee4f4.md)
- [004eef84](../004ee/004eef84.md)
- [004f3c20](../004f3/004f3c20.md)
- [004f7afc](../004f7/004f7afc.md)
- [004f8244](../004f8/004f8244.md)
- [004f9934](../004f9/004f9934.md)
- [00503408](../00503/00503408.md)
- [00503af8](../00503/00503af8.md)
- [00504f50](../00504/00504f50.md)
- [005054cc](../00505/005054cc.md)
- [005060a8](../00506/005060a8.md)
- [0050947c](../00509/0050947c.md)
- [00509f18](../00509/00509f18.md)
- [0050a638](../0050a/0050a638.md)
- [0050b45c](../0050b/0050b45c.md)
- [0050eb14](../0050e/0050eb14.md)
- [0050ef84](../0050e/0050ef84.md)
- [0050fbb8](../0050f/0050fbb8.md)
- [0050fc5c](../0050f/0050fc5c.md)
- [005161d4](../00516/005161d4.md)
- [0051bb34](../0051b/0051bb34.md)
- [0051bd98](../0051b/0051bd98.md)
- [0051bf98](../0051b/0051bf98.md)
- [0051c140](../0051c/0051c140.md)
- [0051ca38](../0051c/0051ca38.md)
- [0051cc00](../0051c/0051cc00.md)
- [0051ce40](../0051c/0051ce40.md)
- [0051d884](../0051d/0051d884.md)
- [005282c4](../00528/005282c4.md)
- [005288f8](../00528/005288f8.md)
- [00528a6c](../00528/00528a6c.md)
- [0052953c](../00529/0052953c.md)
- [0052a0f8](../0052a/0052a0f8.md)
- [0052ae90](../0052a/0052ae90.md)
- [0052bcb4](../0052b/0052bcb4.md)
- [005323ec](../00532/005323ec.md)
- [00532dbc](../00532/00532dbc.md)
- [00536a8c](../00536/00536a8c.md)
- [00539c08](../00539/00539c08.md)
- [00564c60](../00564/00564c60.md)
- [00576334](../00576/00576334.md)
- [0057f1a0](../0057f/0057f1a0.md)
- [00581964](../00581/00581964.md)
- [00581b20](../00581/00581b20.md)
- [00582ff4](../00582/00582ff4.md)
- [0058558c](../00585/0058558c.md)
- [005857bc](../00585/005857bc.md)
- [00585ea0](../00585/00585ea0.md)
- [00587008](../00587/00587008.md)
- [00588344](../00588/00588344.md)
- [005a8954](../005a8/005a8954.md)
- [005a8aac](../005a8/005a8aac.md)
- [005aa9b4](../005aa/005aa9b4.md)
- [005ab094](../005ab/005ab094.md)
- [005ab944](../005ab/005ab944.md)
- [005adef8](../005ad/005adef8.md)
- [005ae3c8](../005ae/005ae3c8.md)
- [005aea7c](../005ae/005aea7c.md)
- [005b1404](../005b1/005b1404.md)
- [005b1ce4](../005b1/005b1ce4.md)
- [005c43a4](../005c4/005c43a4.md)
- [005c8d50](../005c8/005c8d50.md)
- [005c98a4](../005c9/005c98a4.md)
- [005ca880](../005ca/005ca880.md)
- [005d57d0](../005d5/005d57d0.md)
- [0061b7d4](../0061b/0061b7d4.md)
- [0065ec80](../0065e/0065ec80.md)
- [0065f044](../0065f/0065f044.md)
- [0066434c](../00664/0066434c.md)
- [006683dc](../00668/006683dc.md)
- [00669250](../00669/00669250.md)
- [0066e9a0](../0066e/0066e9a0.md)
- [0066ea58](../0066e/0066ea58.md)
- [0066efd0](../0066e/0066efd0.md)
- [0066f090](../0066f/0066f090.md)
- [00671284](../00671/00671284.md)
- [0067133c](../00671/0067133c.md)
- [00671a98](../00671/00671a98.md)
- [00671b58](../00671/00671b58.md)
- [00678d74](../00678/00678d74.md)
- [0067c708](../0067c/0067c708.md)
- [00692224](../00692/00692224.md)
- [006928c4](../00692/006928c4.md)
- [00692bcc](../00692/00692bcc.md)
- [00693650](../00693/00693650.md)
- [006941ac](../00694/006941ac.md)
- [006ad28c](../006ad/006ad28c.md)
- [006ad590](../006ad/006ad590.md)
- [006eccf4](../006ec/006eccf4.md)
- [006fbd74](../006fb/006fbd74.md)
- [006fbfc4](../006fb/006fbfc4.md)
- [0070db34](../0070d/0070db34.md)
- [0070f0b0](../0070f/0070f0b0.md)
- [0071d070](../0071d/0071d070.md)
- [0071d8c4](../0071d/0071d8c4.md)
- [0071e020](../0071e/0071e020.md)
- [0071e6b0](../0071e/0071e6b0.md)
- [0074931c](../00749/0074931c.md)
- [00751cec](../00751/00751cec.md)
- [00759350](../00759/00759350.md)
- [00759430](../00759/00759430.md)
- [0075f8cc](../0075f/0075f8cc.md)
- [007689a0](../00768/007689a0.md)
- [007693f4](../00769/007693f4.md)
- [0076a428](../0076a/0076a428.md)
- [007726fc](../00772/007726fc.md)
- [00776270](../00776/00776270.md)
- [00776bfc](../00776/00776bfc.md)
- [007773bc](../00777/007773bc.md)
- [00777614](../00777/00777614.md)
- [00777958](../00777/00777958.md)
- [00777af0](../00777/00777af0.md)
- [007791f4](../00779/007791f4.md)
- [00779cc8](../00779/00779cc8.md)
- [0077ad2c](../0077a/0077ad2c.md)
- [0077bc14](../0077b/0077bc14.md)
- [0077ce7c](../0077c/0077ce7c.md)
- [0077de20](../0077d/0077de20.md)
- [0077e958](../0077e/0077e958.md)
- [0077f188](../0077f/0077f188.md)
- [0078b0ec](../0078b/0078b0ec.md)
- [0079653c](../00796/0079653c.md)
- [00796d74](../00796/00796d74.md)
- [007bd430](../007bd/007bd430.md)
- [007bf8dc](../007bf/007bf8dc.md)
- [007bfad4](../007bf/007bfad4.md)
- [007c1c70](../007c1/007c1c70.md)
- [007da86c](../007da/007da86c.md)
- [007dbc94](../007db/007dbc94.md)
- [007e5fa4](../007e5/007e5fa4.md)
- [007e7bcc](../007e7/007e7bcc.md)
- [007e7d84](../007e7/007e7d84.md)
- [007eb8f8](../007eb/007eb8f8.md)
- [007f3c28](../007f3/007f3c28.md)
- [007f4120](../007f4/007f4120.md)
- [007fac0c](../007fa/007fac0c.md)
- [008037bc](../00803/008037bc.md)
- [008038c0](../00803/008038c0.md)
- [00803b54](../00803/00803b54.md)
- [00803c58](../00803/00803c58.md)
- [00803fd0](../00803/00803fd0.md)
- [008040d4](../00804/008040d4.md)
- [00887594](../00887/00887594.md)
- [008879f4](../00887/008879f4.md)
- [00887e18](../00887/00887e18.md)
- [0089eb04](../0089e/0089eb04.md)
- [008a0d28](../008a0/008a0d28.md)
- [008a36b4](../008a3/008a36b4.md)
- [008a57e0](../008a5/008a57e0.md)
- [008a58d8](../008a5/008a58d8.md)
- [008b0550](../008b0/008b0550.md)
- [008b0960](../008b0/008b0960.md)
- [008b4328](../008b4/008b4328.md)
- [008b4610](../008b4/008b4610.md)
- [008b47e0](../008b4/008b47e0.md)
- [008b4a2c](../008b4/008b4a2c.md)
- [00970dcc](../00970/00970dcc.md)
- [009749a4](../00974/009749a4.md)
- [00976638](../00976/00976638.md)
- [009772ec](../00977/009772ec.md)
- [00979d0c](../00979/00979d0c.md)
- [0097c594](../0097c/0097c594.md)
- [00980bcc](../00980/00980bcc.md)
- [00989584](../00989/00989584.md)
- [0099a654](../0099a/0099a654.md)
- [009a3648](../009a3/009a3648.md)
- [009c9128](../009c9/009c9128.md)
- [009ce1d0](../009ce/009ce1d0.md)
- [009d2d50](../009d2/009d2d50.md)
- [009d301c](../009d3/009d301c.md)
- [009dd990](../009dd/009dd990.md)
- [00a02e54](../00a02/00a02e54.md)
- [00a081d8](../00a08/00a081d8.md)
- [00a0a488](../00a0a/00a0a488.md)
- [00a24a34](../00a24/00a24a34.md)
- [00a25060](../00a25/00a25060.md)
- [00a26320](../00a26/00a26320.md)
- [00a293b0](../00a29/00a293b0.md)
- [00a52710](../00a52/00a52710.md)
- [00a52904](../00a52/00a52904.md)
- [00a53778](../00a53/00a53778.md)
- [00a5b5b8](../00a5b/00a5b5b8.md)
- [00a60600](../00a60/00a60600.md)
- [00a618b0](../00a61/00a618b0.md)
- [00a63b48](../00a63/00a63b48.md)
- [00aaf8f0](../00aaf/00aaf8f0.md)
- [00ab3338](../00ab3/00ab3338.md)
- [00acaf84](../00aca/00acaf84.md)
- [00acb0ac](../00acb/00acb0ac.md)
- [00ae3268](../00ae3/00ae3268.md)
- [00b4e018](../00b4e/00b4e018.md)
- [00b58fa4](../00b58/00b58fa4.md)
- [00b72a7c](../00b72/00b72a7c.md)
- [00b77d80](../00b77/00b77d80.md)
- [00b77e98](../00b77/00b77e98.md)
- [00b78004](../00b78/00b78004.md)
- [00b78170](../00b78/00b78170.md)
- [00b782e0](../00b78/00b782e0.md)
- [00b78428](../00b78/00b78428.md)
- [00b78570](../00b78/00b78570.md)
- [00b78838](../00b78/00b78838.md)
- [00b78958](../00b78/00b78958.md)
- [00b78ad4](../00b78/00b78ad4.md)
- [00b78c50](../00b78/00b78c50.md)
- [00b78dd0](../00b78/00b78dd0.md)
- [00b78f28](../00b78/00b78f28.md)
- [00b79080](../00b79/00b79080.md)
- [00b7b200](../00b7b/00b7b200.md)
- [00b7c9ac](../00b7c/00b7c9ac.md)
- [00b7e6b4](../00b7e/00b7e6b4.md)
- [00b9a834](../00b9a/00b9a834.md)
- [00b9c6d0](../00b9c/00b9c6d0.md)
- [00b9e070](../00b9e/00b9e070.md)
- [00b9e5b8](../00b9e/00b9e5b8.md)
- [00b9f534](../00b9f/00b9f534.md)
- [00ba7958](../00ba7/00ba7958.md)
- [00ba88e0](../00ba8/00ba88e0.md)
- [00ba8a1c](../00ba8/00ba8a1c.md)
- [00ba8f24](../00ba8/00ba8f24.md)
- [00ba8ffc](../00ba8/00ba8ffc.md)
- [00ba9130](../00ba9/00ba9130.md)
- [00baa21c](../00baa/00baa21c.md)
- [00baa304](../00baa/00baa304.md)
- [00baa794](../00baa/00baa794.md)
- [00baa86c](../00baa/00baa86c.md)
- [00bab330](../00bab/00bab330.md)
- [00baf6a8](../00baf/00baf6a8.md)
- [00bb16a0](../00bb1/00bb16a0.md)
- [00bb1768](../00bb1/00bb1768.md)
- [00bb2120](../00bb2/00bb2120.md)
- [00bb58f8](../00bb5/00bb58f8.md)
- [00bb59c0](../00bb5/00bb59c0.md)
- [00bb6804](../00bb6/00bb6804.md)
- [00bb7500](../00bb7/00bb7500.md)
- [00bc2e00](../00bc2/00bc2e00.md)
- [00bd5f68](../00bd5/00bd5f68.md)

## 呼び出し先

- [00bd6eb8](../00bd6/00bd6eb8.md)
- [00bd7070](../00bd7/00bd7070.md)
- [00bdacd8](../00bda/00bdacd8.md)
- [00bdd260](../00bdd/00bdd260.md)
- [00bde1c0](../00bde/00bde1c0.md)
- [00be1e80](../00be1/00be1e80.md)

## 関連文字列（未確認候補）

~~~text
"_Unwind_Resume"
"_Unwind_Resume() can't return"
"libunwind: %s - %s\n"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 662 bytes

~~~c

void FUN_00bd6fec(long param_1)

{
  undefined *puVar1;
  undefined1 auStack_4a0 [624];
  undefined1 auStack_230 [528];
  
  FUN_00bdacd8(auStack_230);
  if (*(long *)(param_1 + 0x10) == 0) {
    FUN_00bd6eb8(auStack_230,auStack_4a0,param_1);
  }
  else {
    FUN_00bd7070(auStack_230,auStack_4a0,param_1,*(long *)(param_1 + 0x10),
                 *(undefined8 *)(param_1 + 0x18));
  }
  puVar1 = PTR___sF_00c1bc48;
  fprintf((FILE *)(PTR___sF_00c1bc48 + 0x130),"libunwind: %s - %s\n","_Unwind_Resume",
          "_Unwind_Resume() can\'t return");
  fflush((FILE *)(puVar1 + 0x130));
                    /* WARNING: Subroutine does not return */
  abort();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd6fec"></a> `00bd6fec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bd6ff0"></a> `00bd6ff0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd6ff4"></a> `00bd6ff4` | `fc 4f 01 a9` | stp x28,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd6ff8"></a> `00bd6ff8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bd6ffc"></a> `00bd6ffc` | `ff 03 12 d1` | sub sp,sp,#0x480 | `FALL_THROUGH`
<a id="insn-00bd7000"></a> `00bd7000` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bd7004"></a> `00bd7004` | `e0 c3 09 91` | add x0,sp,#0x270 | `FALL_THROUGH`
<a id="insn-00bd7008"></a> `00bd7008` | `34 0f 00 94` | bl 0x00bdacd8 | `UNCONDITIONAL_CALL`
<a id="insn-00bd700c"></a> `00bd700c` | `63 0a 40 f9` | ldr x3,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bd7010"></a> `00bd7010` | `c3 00 00 b5` | cbnz x3,0x00bd7028 | `CONDITIONAL_JUMP`
<a id="insn-00bd7014"></a> `00bd7014` | `e0 c3 09 91` | add x0,sp,#0x270 | `FALL_THROUGH`
<a id="insn-00bd7018"></a> `00bd7018` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bd701c"></a> `00bd701c` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bd7020"></a> `00bd7020` | `a6 ff ff 97` | bl 0x00bd6eb8 | `UNCONDITIONAL_CALL`
<a id="insn-00bd7024"></a> `00bd7024` | `06 00 00 14` | b 0x00bd703c | `UNCONDITIONAL_JUMP`
<a id="insn-00bd7028"></a> `00bd7028` | `64 0e 40 f9` | ldr x4,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bd702c"></a> `00bd702c` | `e0 c3 09 91` | add x0,sp,#0x270 | `FALL_THROUGH`
<a id="insn-00bd7030"></a> `00bd7030` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bd7034"></a> `00bd7034` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bd7038"></a> `00bd7038` | `0e 00 00 94` | bl 0x00bd7070 | `UNCONDITIONAL_CALL`
<a id="insn-00bd703c"></a> `00bd703c` | `33 02 00 90` | adrp x19,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bd7040"></a> `00bd7040` | `c1 b5 ff d0` | adrp x1,0x291000 | `FALL_THROUGH`
<a id="insn-00bd7044"></a> `00bd7044` | `21 ac 20 91` | add x1,x1,#0x82b | `FALL_THROUGH`
<a id="insn-00bd7048"></a> `00bd7048` | `73 26 46 f9` | ldr x19,[x19, #0xc48] | `FALL_THROUGH`
<a id="insn-00bd704c"></a> `00bd704c` | `a2 b6 ff b0` | adrp x2,0x2ac000 | `FALL_THROUGH`
<a id="insn-00bd7050"></a> `00bd7050` | `42 38 18 91` | add x2,x2,#0x60e | `FALL_THROUGH`
<a id="insn-00bd7054"></a> `00bd7054` | `e3 b5 ff d0` | adrp x3,0x295000 | `FALL_THROUGH`
<a id="insn-00bd7058"></a> `00bd7058` | `63 80 1e 91` | add x3,x3,#0x7a0 | `FALL_THROUGH`
<a id="insn-00bd705c"></a> `00bd705c` | `60 c2 04 91` | add x0,x19,#0x130 | `FALL_THROUGH`
<a id="insn-00bd7060"></a> `00bd7060` | `88 2b 00 94` | bl 0x00be1e80 | `UNCONDITIONAL_CALL`
<a id="insn-00bd7064"></a> `00bd7064` | `60 c2 04 91` | add x0,x19,#0x130 | `FALL_THROUGH`
<a id="insn-00bd7068"></a> `00bd7068` | `7e 18 00 94` | bl 0x00bdd260 | `UNCONDITIONAL_CALL`
<a id="insn-00bd706c"></a> `00bd706c` | `55 1c 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd6fec`](#insn-00bd6fec) 範囲 `[['00bd6fec', '00bd7013']]`
  - `CONDITIONAL_JUMP` [`00bd7010`](#insn-00bd7010) → [`00bd7028`](#insn-00bd7028)
  - `FALL_THROUGH` [`00bd7010`](#insn-00bd7010) → [`00bd7014`](#insn-00bd7014)
- ブロック [`00bd7014`](#insn-00bd7014) 範囲 `[['00bd7014', '00bd7027']]`
  - `UNCONDITIONAL_JUMP` [`00bd7024`](#insn-00bd7024) → [`00bd703c`](#insn-00bd703c)
- ブロック [`00bd7028`](#insn-00bd7028) 範囲 `[['00bd7028', '00bd703b']]`
  - `FALL_THROUGH` [`00bd7038`](#insn-00bd7038) → [`00bd703c`](#insn-00bd703c)
- ブロック [`00bd703c`](#insn-00bd703c) 範囲 `[['00bd703c', '00bd706f']]`

## 命令位置別の参照

- [`00bd6ff0`](#insn-00bd6ff0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6ff4`](#insn-00bd6ff4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd7008`](#insn-00bd7008) → [`00bdacd8`](../00bda/00bdacd8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdacd8` · 推定シンボル `None` · 推定型 `None`
- [`00bd7010`](#insn-00bd7010) → [`00bd7028`](#insn-00bd7028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd7020`](#insn-00bd7020) → [`00bd6eb8`](00bd6eb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6eb8` · 推定シンボル `None` · 推定型 `None`
- [`00bd7024`](#insn-00bd7024) → [`00bd703c`](#insn-00bd703c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd7038`](#insn-00bd7038) → [`00bd7070`](../00bd7/00bd7070.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd7070` · 推定シンボル `None` · 推定型 `None`
- [`00bd7044`](#insn-00bd7044) → `0029182b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd7048`](#insn-00bd7048) → `00c1bc48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bd7050`](#insn-00bd7050) → `002ac60e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd7058`](#insn-00bd7058) → `002957a0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd705c`](#insn-00bd705c) → [`010a58b8`](../010a5/010a58b8.md) · `PARAM` · `ANALYSIS` · 関数 `010a58b8` · 推定シンボル `None` · 推定型 `None`
- [`00bd7060`](#insn-00bd7060) → [`00be1e80`](../00be1/00be1e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1e80` · 推定シンボル `None` · 推定型 `None`
- [`00bd7064`](#insn-00bd7064) → [`010a58b8`](../010a5/010a58b8.md) · `PARAM` · `ANALYSIS` · 関数 `010a58b8` · 推定シンボル `None` · 推定型 `None`
- [`00bd7068`](#insn-00bd7068) → [`00bdd260`](../00bdd/00bdd260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd260` · 推定シンボル `None` · 推定型 `None`
- [`00bd706c`](#insn-00bd706c) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd6ff0`](#insn-00bd6ff0)

~~~json
{
  "source": "00bd6ff0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6ff4`](#insn-00bd6ff4)

~~~json
{
  "source": "00bd6ff4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd7008`](#insn-00bd7008)

~~~json
{
  "source": "00bd7008",
  "target": "00bdacd8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd7010`](#insn-00bd7010)

~~~json
{
  "source": "00bd7010",
  "target": "00bd7028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd7020`](#insn-00bd7020)

~~~json
{
  "source": "00bd7020",
  "target": "00bd6eb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd7024`](#insn-00bd7024)

~~~json
{
  "source": "00bd7024",
  "target": "00bd703c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd7038`](#insn-00bd7038)

~~~json
{
  "source": "00bd7038",
  "target": "00bd7070",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd7044`](#insn-00bd7044)

~~~json
{
  "source": "00bd7044",
  "target": "0029182b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029182b",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6c6962756e77696e643a202573202d2025730a00",
  "capture_start": "0029182b",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bd7048`](#insn-00bd7048)

~~~json
{
  "source": "00bd7048",
  "target": "00c1bc48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bc48",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bd7050`](#insn-00bd7050)

~~~json
{
  "source": "00bd7050",
  "target": "002ac60e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac60e",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "5f556e77696e645f526573756d6500",
  "capture_start": "002ac60e",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bd7058`](#insn-00bd7058)

~~~json
{
  "source": "00bd7058",
  "target": "002957a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002957a0",
  "offset": 0,
  "size": 30,
  "datatype": "string",
  "bytes": "5f556e77696e645f526573756d6528292063616e27742072657475726e00",
  "capture_start": "002957a0",
  "capture_bytes": 30,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bd705c`](#insn-00bd705c)

~~~json
{
  "source": "00bd705c",
  "target": "010a58b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd7060`](#insn-00bd7060)

~~~json
{
  "source": "00bd7060",
  "target": "00be1e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd7064`](#insn-00bd7064)

~~~json
{
  "source": "00bd7064",
  "target": "010a58b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd7068`](#insn-00bd7068)

~~~json
{
  "source": "00bd7068",
  "target": "00bdd260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd706c`](#insn-00bd706c)

~~~json
{
  "source": "00bd706c",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
